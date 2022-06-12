import pandas as pd

def get_data(path: str) -> pd.DataFrame:
    """Function loads Data from specific path.
    :param path: data path.
    :return: DataFrame.
    """
    data = pd.read_csv(path)
    return data