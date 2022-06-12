from fastapi import FastAPI
from pydantic import BaseModel
from src.model import make_prediction
from src.features import add_features
# trash
import pandas as pd
import numpy as np

app = FastAPI()


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


@app.post('/predict')
async def trip_duration(trip: TripConfigure):
    trip_params = pd.DataFrame({key: [value] for key, value in dict(trip).items()})
    trip_params = add_features(trip_params, purpose='predict')
    prediction = make_prediction(trip_params)
    prediction = {'prediction': prediction}
    return prediction
    


