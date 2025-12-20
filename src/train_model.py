import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from config import load_config

class ErrorTrainingModel(Exception):
    pass

def create_model():
    config = load_config()
    params = config["model"]["parameters"]

    if config["model"]["type"] == "random_forest":
        model = RandomForestRegressor(**params)
    else: 
        raise ErrorTrainingModel("Wrong model selected")
    
    return model

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    prediction = model.predict(X_test)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)

    return{
        "mae" : mae,
        "rmse" : rmse
    }

def save_model(model):
    config = load_config()
    path = config["output"]["model_dir"]
    joblib.dump(model, path)
    return path
    