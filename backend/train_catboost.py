import pandas as pd
import numpy as np
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split
from src import upload_config, get_data, clean_data, add_features, import_config


def train_catboost(df: pd.DataFrame):
    """Function trains the Catboost model on the input data and returns it.
    :param df: Train dataset
    :return: Catboost trained model
    """
    
    # config
    cfg = import_config('config/params.yaml')

    # data preprocessing
    cat_feature_indices = np.array([0, 5, 6, 8, 9])
    X = df.drop('trip_duration', axis=1)
    X.iloc[:, cat_feature_indices] = X.iloc[:, cat_feature_indices].astype(str)
    y = df.trip_duration
    pool_train = Pool(X, y,cat_features=cat_feature_indices)
    # model fit
    model = CatBoostRegressor(
                                loss_function='RMSE',
                                random_seed=20,
                                early_stopping_rounds=25,
                                verbose=100)
    model.fit(pool_train)
    return model


if __name__ == '__main__':
    path = 'https://github.com/EuMentality/datasets/raw/main/taxi_trip.csv'
    df = add_features(clean_data(get_data(path)), purpose='tuning')
    model = train_catboost(df)
    model.save_model('model/catboost.dump')