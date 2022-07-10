import pandas as pd
import numpy as np
from catboost import CatBoostRegressor


def make_prediction(df: pd.DataFrame) -> int:
    """Function makes taxi trip predictions in minutes  on the input data.
    :param df: input data
    :return: taxi trip duration
    """
    model = CatBoostRegressor().load_model('model/catboost.bin')
    prediction = (np.exp(model.predict(df)[0]) - 1)//60
    return prediction
