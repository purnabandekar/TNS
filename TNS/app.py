from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load traineuvicorn app:app --reloadd model and scaler
model = joblib.load("linear_regression_model.pkl")
scaler = joblib.load("standard_scaler.pkl")


@app.get("/")
def home():
    return {"message": "Manufacturing Output Prediction API is running"}


@app.post("/predict")
def predict(data: list):

    # Convert input to numpy array
    input_data = np.array(data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    return {
        "Predicted_Parts_Per_Hour": float(prediction[0])
    }