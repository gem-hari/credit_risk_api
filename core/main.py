import pickle
import numpy as np
import pandas as pd
import os

def calculate_risk(fico_score, dti, mths, model_type="lr"):
    scaler_path = os.path.join("models", "min_max_scaler.pkl")
    with open(scaler_path, 'rb') as file:
        scaler = pickle.load(file)

    if model_type == "rf":
        model_path = os.path.join("models", "rf_model_trim.pkl")

        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    else:
        model_path = os.path.join("models", "logistic_model_trim.pkl")
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

    input = np.zeros((1,63))
    input[0,22] = fico_score
    input[0,11] = dti
    input[0,29] = mths
    
    transformed_input = scaler.transform(input)
    transformed_input = [[transformed_input[0,22], transformed_input[0,11] ,transformed_input[0,29]]]
    prediction = model.predict(transformed_input)
    return "Accept" if prediction[0] == 0 else "Reject"
#print(calculate_risk(480, 10, 0))