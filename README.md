
## NYC Manhattan Taxi 
<img src = "https://raw.githubusercontent.com/EuMentality/nyc_taxi_trip_proj/main/readme_img/example.png" width = "800"  align = "center" />


Web-Application for predicting taxi trup duration in Manhattan and plotting the optimal route for a trip on the map. 

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

