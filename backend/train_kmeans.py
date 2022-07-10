import logging
import time
import pickle
import pandas as pd
from datetime import datetime, timedelta
from sklearn.cluster import KMeans
from src import get_data, clean_data, import_config


# data preprocessing
def train_kmeans(df: pd.DataFrame):
    """Function trains the Kmeans model on the input data and returns it.
    :param df: Train dataset
    :return: Kmeans trained model
    """
    # config
    cfg = import_config('config/params.yaml')
    n_clusters = cfg['k_means']['n_clusters']
    random_state = cfg['k_means']['random_state']
    # data preprocessing
    df_pickup = df[['pickup_longitude', 'pickup_latitude']]
    df_dropoff = df[['dropoff_longitude', 'dropoff_latitude']]
    cols = ['longitude', 'latitude']
    df_pickup.columns = cols
    df_dropoff.columns = cols
    df_fit = pd.concat([df_pickup, df_dropoff], ignore_index=True)
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df_fit)
    return kmeans


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    path = 'https://github.com/EuMentality/datasets/raw/main/taxi_trip.csv'
    logging.info('Training a model for taxi route clustering!')
    # Data: get, clean
    start_time = time.time()
    logging.info(f'Data preparation starts. {datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")}')
    df = clean_data(get_data(path))
    end_time = time.time()
    execution_time = str(timedelta(seconds=(end_time - start_time))).split('.')[0]
    logging.info(f'Execution time = {execution_time}')
    logging.info(f'Dataset is ready for training. {datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")}') 
    logging.info('Next Stage')
    # K-means fitting & saving
    start_time = time.time()
    logging.info(f'Fitting K-means. {datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")}')
    model = train_kmeans(df)
    pickle.dump(model, open('model/kmeans.pkl', 'wb'))
    end_time = time.time()
    execution_time = str(timedelta(seconds=(end_time - start_time))).split('.')[0]
    logging.info(f'Execution time = {execution_time}')
    logging.info(f'K-means Trained & Saved. {datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")}')