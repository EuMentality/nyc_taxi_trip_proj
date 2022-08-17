
## NYC Manhattan Taxi 
<img src = "https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/example.png" width = "800"  align = "center" />


Web-Application for predicting taxi trip duration in Manhattan and plotting the optimal route for a trip on the map. 

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
Dataset from this [competition](https://www.kaggle.com/c/nyc-taxi-trip-duration).

The data was cleared of irrelevant trips that were started or ended outside of Manhattan. Taxi trips was filtered by the dividing line, which was built along 13 bridges leading to Manhattan. 

<p align="center">
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_1.png" width = "700" />
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_2.png" width = "700" />
  <img src="https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/start_end_3.png" width = "700" />
</p>

Why was it necessary to choose trips made in Manhattan? The smaller the search area, the faster the optimal route is searched, since the service has a performance limit.




