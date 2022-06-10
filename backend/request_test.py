import requests

path = "http://localhost:5005"

features = {
    'pickup_longitude': -73.982155,
    'pickup_latitude': 40.767937,
    'dropoff_longitude': -73.964630,
    'dropoff_latitude': 40.765602,
    'pickup_datetime': '2016-03-14 17:24:55',
    'passenger_count': 1,
    'vendor_id': 2,
    'store_and_fwd_flag': 'N'
    }

resp = requests.post(f'{path}/predict',
                    json=features)
print(resp.json())