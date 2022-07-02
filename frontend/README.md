Frontend Organization
===============
    ├── config
    │   └── params.yaml          <- Map & URL Backend configuration.
    │
    ├── src
    │   ├── __init__.py          <- Make src a Python module.
    │   ├── build_route.py       <- Rout search on the map.
    │   ├── config.py            <- Import config.
    │   └── predict.py           <- Send post request to Backend for predicting Trip Duration
    │                     
    ├── README.md                <- Backend Description.
    │
    ├── app.py                   <- FastAPI backend app.
    │
    ├── requirements.txt         <- Requirements for env.
    │
    └── train.py                 <- Training & Saving model.