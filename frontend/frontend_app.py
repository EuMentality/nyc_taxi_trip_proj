import pytz
import streamlit as st
import osmnx as ox
from PIL import Image
from datetime import datetime
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
from src import find_shortest_route, predict_trip_duration, upload_config

st.set_page_config(layout="wide")
# 1. Upload Config
cfg = upload_config('config/params.yaml')
url_backend = cfg['backend']['url']
map_with = cfg['map']['width']
map_height = cfg['map']['height']

# 2. Sidebar Settings
st.sidebar.header('Information About The Trip')
st.sidebar.subheader('Follow this link:  [Google Maps](https://www.google.com/maps/place/Manhattan,+New+York,+NY,+USA/@40.7604865,-73.9767845,14342m/data=!3m1!1e3!4m5!3m4!1s0x89c2588f046ee661:0xa0b3281fcecc08c!8m2!3d40.7830603!4d-73.9712488)')
page_names = ['Enter Address', 'Enter Coordinates']
page = st.sidebar.radio('Choose The Navigation Type', page_names)
if page == 'Enter Coordinates':
    pickup_latitude = st.sidebar.number_input('Pickup Latitude', 40.700000, 40.840010, 40.765990, step=0.00001, format="%.6f")
    pickup_longitude = st.sidebar.number_input('Pickup Longitude', -74.020000, -73.930100, -73.980000, step=0.00001, format="%.6f")
    dropoff_latitude = st.sidebar.number_input('Dropoff Latitude', 40.700000, 40.840010, 40.770000, step=0.00001, format="%.6f")
    dropoff_longitude = st.sidebar.number_input('Dropoff Longitude', -74.020000, -73.9301, -73.990000, step=0.00001, format="%.6f")
    pickup_datetime = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f'Time Now in NYC:  {str(pickup_datetime)}')
    passenger_count = st.sidebar.slider('Number of Passengers', 1, 6, 1)
    
else:
    pickup_address = st.sidebar.text_input('Pickup Address', 'Empire State Building')
    dropoff_address = st.sidebar.text_input('Dropoff Address', 'Museum of the NYC')
    loc = Nominatim(user_agent="GetLoc")
    getloc_start = loc.geocode(pickup_address)
    getloc_end = loc.geocode(dropoff_address)
    pickup_latitude = getloc_start.latitude
    pickup_longitude = getloc_start.longitude
    dropoff_latitude = getloc_end.latitude
    dropoff_longitude = getloc_end.longitude
    pickup_datetime = datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f'Time Now in NYC:  {str(pickup_datetime)}')
    passenger_count = st.sidebar.slider('Number of Passengers', 1, 6, 1)

trip_params = {'pickup_latitude': pickup_latitude,
                'pickup_longitude': pickup_longitude, 
                'dropoff_latitude': dropoff_latitude,
                'dropoff_longitude': dropoff_longitude,
                'pickup_datetime': pickup_datetime,
                'passenger_count': passenger_count}
                
start_trip_coords = (pickup_latitude, pickup_longitude)
end_trip_coords = (dropoff_latitude, dropoff_longitude)

# 3. Main Page Seggings
st. markdown("<h1 style='text-align: center; color: black;'>Manhattan Taxi Trip </h1>", unsafe_allow_html=True)
ox.config(log_console=True, use_cache=True)
if st.sidebar.button('Predict Trip Duration!'):
    col1, col2, col3 = st.columns([2, 7, 1])
    with col1:
        st.write("")
    with col2:
        ans = predict_trip_duration(url_backend, trip_params)
        ans_text = f'The duration of your trip will be {int(ans["prediction"])} minutes!'
        with st.spinner('The route of the trip is being built ^_^  :oncoming_taxi:'):
                shortest_route = find_shortest_route(start_trip_coords, end_trip_coords)
                st_data = folium_static(shortest_route, width=map_with, height=map_height)
        st.success(ans_text)
    with col3:
        st.write("")
else:
    col1, col2, col3 = st.columns([0.8, 7, 1])
    with col1:
        st.write("")
    with col2:
        text = "Enter Trip Parameters: Left Panel"
        st. markdown(f"<h5 style='text-align: center; color: gray;'>{text} </h5> ", unsafe_allow_html=True)
        # Image
        image = Image.open('src/ptr_manh.jpg')
        st.image(image)
    with col3:
        st.write("")

