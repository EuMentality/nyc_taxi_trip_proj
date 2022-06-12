import pandas as pd
import numpy as np
from catboost import CatBoostRegressor


def make_prediction(df: pd.DataFrame) -> int:
    """Function makes taxi trip predictions in minutes  on the input data.
    :param df: input data
    :return: taxi trip duration
    """
    cat_feature_indices = np.array([0, 1, 6, 8, 9, 10, 11])
    df.iloc[:, cat_feature_indices] = df.iloc[:, cat_feature_indices].astype(str)
    model = CatBoostRegressor().load_model('model/catboost.dump')
    prediction = (np.exp(model.predict(df)[0]) - 1)//60
    return prediction
