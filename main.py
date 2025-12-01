from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model_all = joblib.load("poverty_all_model.pkl")
model_under18 = joblib.load("poverty_under18_model.pkl")

@app.get("/")
def home():
    return {"message": "Poverty prediction API working"}

@app.post("/predict")
def predict(
    income: float,
    poverty_last_year: float,
    income_last_year: float,
    avg_3yr: float
):
    features = np.array([[income, poverty_last_year, income_last_year, avg_3yr]])

    pred_all = model_all.predict(features)[0]
    pred_under18 = model_under18.predict(features)[0]

    return {
        "poverty_all_prediction": float(pred_all),
        "poverty_under18_prediction": float(pred_under18)
    }
