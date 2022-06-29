import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Function cleans data from outliers and irrelevant trips.
    :param df: raw dataframe.
    :return df: cleared df.
    """
    latitude_min, latitude_max = 40.700, 40.85
    longitude_min, longitude_max = -74.02, -73.93
    mask_1 = df['dropoff_latitude'].between(latitude_min, latitude_max)
    mask_2 = df['pickup_latitude'].between(latitude_min, latitude_max)
    mask_3 = df['dropoff_longitude'].between(longitude_min,longitude_max)
    mask_4 = df['pickup_longitude'].between(longitude_min, longitude_max)
    mask_5 = df['vendor_id'] == 1
    mask_6 = df['store_and_fwd_flag'] == 'N'
    mask_7 = df['passenger_count'] != 0
    mask = mask_1 & mask_2 & mask_3 & mask_4 & mask_5 & mask_6 & mask_7
    df = df[mask].reset_index(drop=True)
    df = df.drop(['vendor_id', 'store_and_fwd_flag'], axis=1)
    return df
