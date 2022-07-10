import logging
import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from catboost import CatBoostRegressor, Pool
from src import get_data, clean_data, add_features, import_config


def train_catboost(df: pd.DataFrame):
    """Function trains the Catboost model on the input data and returns it.
    :param df: Train dataset
    :return: Catboost trained model
    """
    # config
    cfg = import_config('config/params.yaml')
    catboost_params = cfg['catboost']
    catboost_params['verbose'] = 400
    # data preprocessing
    cat_feature_indices = np.array([0, 5, 6, 7, 8, 9, 11])
    X = df.drop('trip_duration', axis=1)
    y = df.trip_duration
    pool_train = Pool(X, y,cat_features=cat_feature_indices)
    # Model training
    model = CatBoostRegressor(**catboost_params)
    model.fit(pool_train)
    return model


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    path = 'https://github.com/EuMentality/datasets/raw/main/taxi_trip.csv'
    logging.info('Training a model for predicting the duration of a taxi ride!')
    # Data: get, clean, add features
    start_time = time.time()
    logging.info(f'Data preparation starts. {datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")}')
    df = add_features(clean_data(get_data(path)), path_kmeans='model/kmeans.pkl', purpose='tuning')
    end_time = time.time()
    execution_time = str(timedelta(seconds=(end_time - start_time))).split('.')[0]
    logging.info(f'Execution time = {execution_time}')
    logging.info(f'Dataset is ready for training. {datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")}') 
    logging.info('Next Stage')
    # Catboost fitting & saving
    start_time = time.time()
    logging.info(f'Fitting Catboost. {datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")}')
    model = train_catboost(df)
    model.save_model('model/catboost.dump')
    end_time = time.time()
    execution_time = str(timedelta(seconds=(end_time - start_time))).split('.')[0]
    logging.info(f'Execution time = {execution_time}')
    logging.info(f'Catboost Trained & Saved. {datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")}')