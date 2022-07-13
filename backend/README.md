Backend Organization
===============
    ├── config
    │   └── params.yaml          <- Catboost train and validation params.
    │
    ├── model
    │   ├── catboost.bin         <- Trained Catboost model.
    │   └── kmeans.pkl           <- Trained K-means model.
    │ 
    ├── notebooks
    │   ├── 1_EDA.ipynb          <- EDA.
    │   └── 2_tuning.ipynb       <- Tuning params with Optuna, Quality Estimation, Feature Importance.
    │
    ├── src
    │   ├── __init__.py          <- Make src a Python package.
    │   ├── add_features.py      <- Add features for tuning or predicting.
    │   ├── clean_data.py        <- Data cleaning.
    │   ├── config.py            <- Import Configuration.
    │   ├── get_data.py          <- Download raw data from storage.
    │   └── make_prediction.py   <- Predict trip duration: request from Streamlit.
    │          
    ├── .dockerignore            <- Dockerignore file.
    │
    ├── Dockerfile               <- Dockerfile for backend image building.
    │
    ├── README.md                <- Backend Repo Description.
    │
    ├── app.py                   <- FastAPI backend app.
    │
    ├── requirements.txt         <- Dependencies for container env.
    │
    ├── requirements_work.txt    <- Dependencies that were used during the project.
    │
    ├── train_catboost.py        <- Training & Saving Catboost.
    └── train_kmeans.py          <- Training & Saving K-means.  