import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from catboost import CatBoostRegressor

# trash
import pandas as pd

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

def data_preprocess(x):
    for key, value in dict(x).items():
        
    df = pd.DataFrame(data=dict(x))
    print(df)



@app.post('/predict')
async def trip_duration(trip: TripConfigure):
    data_preprocess(trip)
    


