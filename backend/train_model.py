import yaml
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from src.data import get_data, clean_data
from src.features import add_features

# config params
def train(df: pd.DataFrame):
    """Function trains the Catboost model on the input data and returns it.
    :param df: Train dataset
    :return: Catboost trained model
    """
    def config():
        with open("config/params.yaml", "r") as f:
                return yaml.safe_load(f)
    #config
    cfg = config()
    ##data split cfg
    test_size = cfg['data_split']['test_size']
    test_split_seed = cfg['data_split']['test_split_seed']
    valid_size = cfg['data_split']['valid_size']
    valid_split_seed = cfg['data_split']['valid_split_seed']
    ##tuning params
    # data splitting
    cat_feature_indices = np.array([0, 1, 6, 8, 9, 10, 11])
    X = df.drop('trip_duration', axis=1)
    X.iloc[:, cat_feature_indices] = X.iloc[:, cat_feature_indices].astype(str)
    y = df.trip_duration
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=test_split_seed)
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=valid_size, random_state=valid_split_seed)
    # model fit
    model = CatBoostRegressor(
            loss_function='RMSE',
            random_seed=20,
            early_stopping_rounds=25,
            verbose=100)
    model.fit(X_train, y_train,
              cat_features=cat_feature_indices,
              eval_set=(X_valid, y_valid))

    return model


if __name__ == '__main__':
    path = 'https://github.com/EuMentality/datasets/raw/main/taxi_trip.csv'
    df = get_data(path)
    df = clean_data(df)
    df = add_features(df, purpose='tuning')
    model = train(df)
    model.save_model('model/catboost.dump')