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
    mask = mask_1 & mask_2 & mask_3 & mask_4
    df = df[mask].reset_index(drop=True)
    return df
