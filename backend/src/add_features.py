import pickle
import pandas as pd
import numpy as np


def add_features(data: pd.DataFrame, path_kmeans: str, purpose: str = 'predict') -> pd.DataFrame:
    """Data proccessing for tuning model or prediction.
    :param data: df 
    :param purpose: df purpose, train model or predict
    :return df: df with generated features
    """
    df = data.copy()
    # time col to datetime
    df['pickup_datetime'] = pd.to_datetime(df.pickup_datetime)
    # month, weekday, hour of pickup date
    df['pickup_month'] = df['pickup_datetime'].dt.month
    df['pickup_weekday'] = df['pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    df['high_traffic'] = df['pickup_hour'].apply(lambda x: 1 if  8 <= x <= 20 else 0)
    # anomaly day
    anomaly_days = [pd.to_datetime('2016-01-23'), pd.to_datetime('2016-01-24')]
    df['anomaly'] = df.pickup_datetime.between(anomaly_days[0], anomaly_days[1], inclusive='both').astype(int)
    df.drop('pickup_datetime', axis=1, inplace=True)
    # estimation of the trip distance
    meas_ang = 0.506 # 29 angle degree = 0.506 radian
    df['diff_latitude'] = (df['dropoff_latitude'] - df['pickup_latitude']).abs()*111
    df['diff_longitude'] = (df['dropoff_longitude'] - df['pickup_longitude']).abs()*80
    df['Euclidean'] = (df.diff_latitude**2 + df.diff_longitude**2)**0.5 
    df['delta_manh_long'] = (df.Euclidean*np.sin(np.arctan(df.diff_longitude / df.diff_latitude)-meas_ang)).abs()
    df['delta_manh_lat'] = (df.Euclidean*np.cos(np.arctan(df.diff_longitude / df.diff_latitude)-meas_ang)).abs()
    df['manh_length'] = df.delta_manh_long + df.delta_manh_lat
    df.drop(['diff_latitude', 'diff_longitude', 'Euclidean', 'delta_manh_long', 'delta_manh_lat'], axis=1, inplace=True)
    # n_passengers
    df['passenger_count'] = df['passenger_count'].apply(lambda x: 1 if (x < 5) else 2)
    # route with kmeans
    kmeans = pickle.load(open(path_kmeans, 'rb'))
    df['dropoff_cluster'] = kmeans.predict(df[['dropoff_longitude', 'dropoff_latitude']].rename(columns={'dropoff_longitude': 'longitude', 'dropoff_latitude': 'latitude'}))
    df['pickup_cluster'] = kmeans.predict(df[['pickup_longitude', 'pickup_latitude']].rename(columns={'pickup_longitude': 'longitude', 'pickup_latitude': 'latitude'}))
    df['route'] = (df.dropoff_cluster.astype(str) + ' ' + df.pickup_cluster.astype(str)).str.split().apply(sorted).apply(lambda x: x[0] + '_' + x[1])


    # list of needed cols
    columns = ['passenger_count', 'pickup_longitude', 'pickup_latitude',
               'dropoff_longitude', 'dropoff_latitude', 'pickup_month',
               'pickup_weekday', 'pickup_hour', 'high_traffic', 'anomaly', 'manh_length', 'route']

    if purpose == 'tuning':
        df.trip_duration = np.log1p(df.trip_duration)
        columns.append('trip_duration')

    df = df[columns]
    return df