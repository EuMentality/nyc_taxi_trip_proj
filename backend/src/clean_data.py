import pandas as pd


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Function cleans data from outliers and irrelevant trips.
    :param df: raw dataframe.
    :return df: cleared df.
    """
    def find_line(A, B):
        y_1, x_1 = A
        y_2, x_2 = B
        k = (y_2 - y_1)/(x_2 - x_1)
        b = y_1 - k*x_1
        return k, b

    df = data.copy()
    mask_1 = df['vendor_id'] == 1
    mask_2 = df['store_and_fwd_flag'] == 'N'
    mask_3 = df['passenger_count'] != 0
    mask = mask_1 & mask_2 & mask_3
    df = df[mask].reset_index(drop=True)
    df = df.drop(['vendor_id', 'store_and_fwd_flag'], axis=1)

    # 13 Bridges in Manhattan
    coords = {}
    coords['middle_henry_bridge'] = (40.877758, -73.922214)
    coords['middle_broadway_bridge'] = (40.873689, -73.910933)
    coords['middle_washington_bridge'] = (40.851470, -73.952140)
    coords['middle_linkoln_tunnel'] = (40.762886, -74.009588)
    coords['middle_holland_tunnel'] = (40.727318, -74.021006)
    coords['middle_brooklyn_bridge'] = (40.704914, -73.995546)
    coords['middle_williamsburg_bridge'] = (40.713333, -73.971641)
    coords['middle_midtown_tunnel'] = (40.744429, -73.963135)
    coords['middle_quins_bridge'] = (40.755947, -73.952374)
    coords['middle_kennedy_bridge'] = (40.798973, -73.919060)
    coords['middle_avenue_bridge'] = (40.807628, -73.932374)
    coords['middle_river_bridge'] = (40.834455, -73.934541)
    coords['middle_heights_bridge'] = (40.862674, -73.914647)

    # Building Borders (Manhattan)
    borders_coefs = {}
    borders_list = [('middle_henry_bridge', 'middle_broadway_bridge'), ('middle_washington_bridge', 'middle_linkoln_tunnel'),
                    ('middle_linkoln_tunnel', 'middle_holland_tunnel'), ('middle_brooklyn_bridge', 'middle_williamsburg_bridge'),
                    ('middle_williamsburg_bridge', 'middle_midtown_tunnel'), ('middle_midtown_tunnel', 'middle_quins_bridge'),
                    ('middle_kennedy_bridge', 'middle_avenue_bridge'), ('middle_avenue_bridge', 'middle_river_bridge'),
                    ('middle_river_bridge', 'middle_heights_bridge')]
    for border in borders_list:
        a, b = border
        borders_coefs[f'{a.split("_")[1]}_{b.split("_")[1]}_path'] = find_line(coords[a], coords[b])

    for border_path, border_coef in borders_coefs.items():
        k, b = border_coef
        df[f'{border_path}_drop'] = k*df.dropoff_longitude + b
        df[f'{border_path}_pick'] = k*df.pickup_longitude + b

    # Filtering Irrelevant Trips
    mask_0_1 = df.henry_broadway_path_pick >= df.pickup_latitude
    mask_0_2 = df.henry_broadway_path_drop >= df.dropoff_latitude
    mask_0 = mask_0_1 & mask_0_2

    mask_1_1 = df.washington_linkoln_path_pick >= df.pickup_latitude
    mask_1_2 = df.washington_linkoln_path_drop >= df.dropoff_latitude
    mask_1 = mask_1_1 & mask_1_2

    mask_2_1 = df.linkoln_holland_path_pick >= df.pickup_latitude
    mask_2_2 = df.linkoln_holland_path_drop >= df.dropoff_latitude
    mask_2 = mask_2_1 & mask_2_2

    mask_3_1 = df.brooklyn_williamsburg_path_pick <= df.pickup_latitude
    mask_3_2 = df.brooklyn_williamsburg_path_drop <= df.dropoff_latitude
    mask_3 = mask_3_1 & mask_3_2

    mask_4_1 = df.williamsburg_midtown_path_pick <= df.pickup_latitude
    mask_4_2 = df.williamsburg_midtown_path_drop <= df.dropoff_latitude
    mask_4 = mask_4_1 & mask_4_2

    mask_5_1 = df.midtown_quins_path_pick <= df.pickup_latitude
    mask_5_2 = df.midtown_quins_path_drop <= df.dropoff_latitude
    mask_5 = mask_5_1 & mask_5_2

    mask_6_1 = df.kennedy_avenue_path_pick >= df.pickup_latitude
    mask_6_2 = df.kennedy_avenue_path_drop >= df.dropoff_latitude
    mask_6 = mask_6_1 & mask_6_2

    mask_7_1 = df.avenue_river_path_pick >= df.pickup_latitude
    mask_7_2 = df.avenue_river_path_drop >= df.dropoff_latitude
    mask_7 = mask_7_1 & mask_7_2

    mask_8_1 = df.river_heights_path_pick <= df.pickup_latitude
    mask_8_2 = df.river_heights_path_drop <= df.dropoff_latitude
    mask_8 = mask_8_1 & mask_8_2

    mask = mask_0 & mask_1 & mask_2 & mask_3 & (mask_4 | mask_5) & ((mask_6 | mask_7 | mask_8))
    df = df[mask].reset_index(drop=True)
    cols = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude',
            'trip_duration', 'pickup_datetime', 'passenger_count',]
    return df[cols]

