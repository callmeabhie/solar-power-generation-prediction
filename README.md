# Solar Power Generation Prediction

## 📌 Project Overview

This project predicts solar power generation using Machine Learning techniques. The project uses environmental and weather-related features to estimate the amount of solar power generated.

The model is built using Python and XGBoost and is deployed using Streamlit for interactive predictions.

## 🎯 Objective

To develop a machine learning regression model that can accurately predict solar power generation based on weather and environmental conditions.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Jupyter Notebook

## 📊 Dataset Features

The dataset contains features such as:

- Distance to Solar Noon
- Temperature
- Wind Direction
- Wind Speed
- Sky Cover
- Visibility
- Humidity
- Average Wind Speed
- Average Pressure

### Target Variable

- Power Generated

## 🔄 Project Workflow

1. Data Collection
2. Data Loading
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Data Preprocessing
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

## 🤖 Machine Learning Model

The project uses **XGBoost Regressor** to predict solar power generation.

The trained model and scaler are saved using Pickle:

- `xgboost_model.pkl`
- `scaler.pkl`

## 📈 Model Evaluation

The model was evaluated using regression metrics including:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## 🚀 Streamlit Application

A Streamlit application (`app.py`) is included to provide an interactive interface for making solar power generation predictions.

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/callmeabhie/solar-power-generation-prediction.git
