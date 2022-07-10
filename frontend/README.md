Frontend Organization
===============
    ├── config
    │   └── params.yaml          <- URL-Backend & Map configuration.
    │
    ├── src
    │   ├── __init__.py          <- Make src a Python module.
    │   ├── build_route.py       <- Rout on the map.
    │   ├── config.py            <- Import config.
    │   └── predict.py           <- Send post request to Backend for predicting Trip Duration.
    │                     
    ├── frontend_app.py          <- Streamlit "frontend" app.
    │
    ├── README.md                <- Frontend decription.
    │
    └── requirements.txt         <- Requirements for env.