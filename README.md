
# NYC Manhattan Taxi 
<img src = "https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/example.png" width = "800"  align = "center" />


Web-Application for predicting taxi trip duration in Manhattan and plotting optimal route for a trip on the map. 

In this pet-project, we serve catboost model for predicting trip duration using FastAPI for the backend service and streamlit for the frontend service. docker-compose orchestrates the two services and allows communication between them.

### Repository Organization 

    ├── backend              <- backend-service repo.
    │
    ├── frontend             <- frontend-service repo.
    │
    ├── readme_img           <- imgs for README.
    │
    ├── .gitignore           <- gitignore file.
    │                     
    ├── docker-compose.yml   <- docker-compose file.
    │
    └── README.md            <- Pet-Project description.

### Run app locally
To run the app in a machine running Docker and docker-compose, run:

    docker-compose build
    docker-compose up

Streamlit UI - http://localhost:8501

FastAPI docs - http://localhost:8000/docs 


### Try the app
- Frontend deployed on Streamlit.share, visit [Web-App](https://eumentality-stmlt-nyc-main-app-p4lk5n.streamlitapp.com/). 
- Backend deployed on the Heroku cloud platform, see the [docs](https://taxi-nyc-fastapi.herokuapp.com/docs).

### About the project
#### 1. Data preparation
Dataset from this [competition](https://www.kaggle.com/c/nyc-taxi-trip-duration).

##### 1.1 Data cleaning
The data was cleared of irrelevant trips that were started or ended outside of Manhattan. Taxi trips was filtered by the dividing line, which was built along 13 bridges leading to Manhattan. 

<p align="center">
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_1.png" width = "650" />
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_2.png" width = "650" />
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_3.png" width = "650" />
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/clustering.png" width = "450" />
</p>

Why was it necessary to choose trips made in Manhattan? The smaller search area, the faster optimal route is searched, cause the service has a performance limit.

##### 1.2 Feature Preprocessing

Features: 

    - manh_length                  <- Manhattan distance estimation btw start-end of the trip.
    - route                        <- Route of the trip is based on the formed clusters. 
    - time-based features          <- hour, weekday, high traffic(binary), etc.
    - coordinates-based features   <- latitude/longitude.

[Read more](https://github.com/EuMentality/nyc_taxi_trip_proj/blob/main/backend/notebooks/1_EDA.ipynb) about data cleaning & feature preprocessing in the presentation format (notebook).
#### 2. Fit-Predict
##### 2.1 Model training
Catboost model was used for training.
Loss-function MSLE, since we need the function which're penalize for under-prediction more than through over-prediction.  

To search hyperparameters was used Optuna.


##### 2.2 Model quality estimation

| Data | MSLE | MAE         | $R^2$|
| ---  | ---  | ---         | --- |
| Train| 0.08 | 2.27 minutes| 0.84 |
| Test | 0.12 | 2.42 minutes| 0.75 |

[Read more](https://github.com/EuMentality/nyc_taxi_trip_proj/blob/main/backend/notebooks/1_EDA.ipynb) about `2.1` & `2.2` (notebook).

#### 3. How it works!


<p align="center">
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/hiw_main.png" width = "650" />
</p>

