import requests


def predict_trip_duration(url: str, json_obj: dict) -> dict:
    """Function sends a post request to backend server in order to calculate the duration.
    :param url: Backend server
    :param json_obj: Trip params
    :return: dict with trip duration 
    """
    resp = requests.post(f'{url}', json=json_obj)
    return resp.json()