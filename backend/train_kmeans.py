import pickle
import pandas as pd
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
    path = 'https://github.com/EuMentality/datasets/raw/main/taxi_trip.csv'
    df = clean_data(get_data(path))
    model = train_kmeans(df)
    pickle.dump(model, open('model/kmeans.pkl', 'wb'))
