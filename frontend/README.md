Frontend Organization
===============
    ├── config
    │   └── params.yaml          <- URL-Backend & Map configuration.
    │
    ├── src
    │   ├── __init__.py          <- Make src a Python module.
    │   ├── build_route.py       <- Rout on the map.
    │   ├── config.py            <- Import config.
    │   ├── predict.py           <- Post request to Backend for predicting Trip Duration.
    │   └── ptr_manh.jpg         <- Main picture.
    │
    ├── .dockerignore            <- Dockerignore file.
    │
    ├── Dockerfile               <- Dockerfile for "frontend" image building.
    │                     
    ├── README.md                <- Frontend Repo Description.
    │
    ├── frontend_app.py          <- Streamlit "frontend" app.
    │
    └── requirements.txt         <- Requirements for env.