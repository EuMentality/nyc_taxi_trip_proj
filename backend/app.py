import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from catboost import CatBoostRegressor

# trash
import pandas as pd
import numpy as np

app = FastAPI()
model = CatBoostRegressor().load_model('model/catboost_test.dump')


class TripConfigure(BaseModel):
    """
    Input Features Validation for the ml model
    """
    pickup_latitude: float
    pickup_longitude: float
    dropoff_latitude: float
    dropoff_longitude: float
    pickup_datetime: str
    passenger_count: int
    vendor_id: int
    store_and_fwd_flag: str

def preprocess(asd):
    df = asd
    df.pickup_datetime = pd.to_datetime(df.pickup_datetime)
    df['pickup_month'] = df['pickup_datetime'].dt.month
    df['pickup_weekday'] = df['pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    df['high_traffic'] = df['pickup_hour'].apply(lambda x: 1 if  8 <= x <= 20 else 0)
    anomaly_days = [pd.to_datetime('2016-01-23'), pd.to_datetime('2016-01-24')]
    df['anomaly'] = df.pickup_datetime.between(anomaly_days[0], anomaly_days[1], inclusive='both').astype(int)
    df.drop('pickup_datetime', axis=1, inplace=True)
    meas_ang = 0.506
    df['diff_latitude'] = (df['dropoff_latitude'] - df['pickup_latitude']).abs()*111
    df['diff_longitude'] = (df['dropoff_longitude'] - df['pickup_longitude']).abs()*80
    df['Euclidean'] = (df.diff_latitude**2 + df.diff_longitude**2)**0.5 
    df['delta_manh_long'] = (df.Euclidean*np.sin(np.arctan(df.diff_longitude / df.diff_latitude)-meas_ang)).abs()
    df['delta_manh_lat'] = (df.Euclidean*np.cos(np.arctan(df.diff_longitude / df.diff_latitude)-meas_ang)).abs()
    df['manh_length'] = df.delta_manh_long + df.delta_manh_lat
    df.drop(['diff_latitude', 'diff_longitude', 'Euclidean', 'delta_manh_long', 'delta_manh_lat'], axis=1, inplace=True)
    df['passenger_count'] = df['passenger_count'].apply(lambda x: -1 if (x in [7,8,9,0]) else x)
    df = df[['vendor_id', 'passenger_count', 'pickup_longitude', 'pickup_latitude',
            'dropoff_longitude', 'dropoff_latitude', 'store_and_fwd_flag',
            'pickup_month', 'pickup_weekday', 'pickup_hour', 'high_traffic',
            'anomaly', 'manh_length']]
    cat_feature_indices = np.array([0, 1, 6, 8, 9, 10, 11])
    df.iloc[:, cat_feature_indices] = df.iloc[:, cat_feature_indices].astype(str)
    return df


def data_preprocess(x):
    data = {key: [value] for key, value in dict(x).items()}    
    data = pd.DataFrame(data=data)
    data = preprocess(data)
    return data



@app.post('/predict')
async def trip_duration(trip: TripConfigure):
    trip = data_preprocess(trip)
    prediction = np.exp(model.predict(trip)[0]) - 1
    prediction = {'prediction': prediction}
    return prediction
    


