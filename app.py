import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

st.set_page_config(page_title="Solar Power Generation Prediction", layout="centered")

MODEL_PATH = r"C:\Users\Friends\Downloads\xgboost_model.pkl"
SCALER_PATH = r"C:\Users\Friends\Downloads\scaler.pkl"

@st.cache_resource
def load_model_and_scaler():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at: {MODEL_PATH}")
        st.stop()
    if not os.path.exists(SCALER_PATH):
        st.error(f"Scaler file not found at: {SCALER_PATH}")
        st.stop()
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

model, scaler = load_model_and_scaler()

st.title(" 🔆 Solar Power Generation Prediction")

distance_to_solar_noon = st.slider("Distance to Solar Noon", 0.0, 1.0, 0.5)
temperature = st.slider("Temperature (Fahrenheit)", 0, 120, 75)
wind_direction = st.slider("Wind Direction (Degrees)", 0, 360, 180)
wind_speed = st.slider("Wind Speed (mph)", 0.0, 50.0, 8.0)
sky_cover = st.slider("Sky Cover (0–8)", 0, 8, 3)
visibility = st.slider("Visibility (miles)", 0.0, 10.0, 10.0)
humidity = st.slider("Humidity (%)", 0, 100, 50)
average_wind_speed_period = st.slider("Average Wind Speed (period) (mph)", 0.0, 50.0, 8.0)
average_pressure_period = st.slider("Average Pressure (period) (inches Hg)", 28.0, 32.0, 29.9)

input_data = pd.DataFrame([{
    "distance-to-solar-noon": distance_to_solar_noon,
    "temperature": temperature,
    "wind-direction": wind_direction,
    "wind-speed": wind_speed,
    "sky-cover": sky_cover,
    "visibility": visibility,
    "humidity": humidity,
    "average-wind-speed-(period)": average_wind_speed_period,
    "average-pressure-(period)": average_pressure_period
}])

try:
    scaled_input = scaler.transform(input_data)
except Exception as e:
    st.error("Scaler failed.")
    st.code(str(e))
    st.stop()

if st.button("Predict Power Generation"):
    try:
        prediction = model.predict(scaled_input)[0]
        st.success(f"Predicted Power Generated: {prediction:.2f} units")
    except Exception as e:
        st.error("Prediction failed.")
        st.code(str(e))
