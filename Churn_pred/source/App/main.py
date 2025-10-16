import streamlit as st
import numpy as np
import joblib
import pandas as pd

model = joblib.load("../Model/model.pkl")

st.title("📞 Telco Customer Churn Prediction")
st.write("Enter customer details to predict if they are likely to churn.")

gender = st.selectbox("gender", ["Male", "Female"])

SeniorCitizen = st.selectbox("SeniorCitizen", [0, 1])

Partner = st.selectbox("Partner", ["Yes", "No"])

Dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input("tenure", value=0, step=1, min_value=0)

PhoneService = st.selectbox("PhoneService", ["Yes", "No"])

MultipleLines = st.selectbox("MultipleLines", ["Yes", "No", "No phone service"])

InternetService = st.selectbox("InternetService", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("OnlineSecurity", ["Yes", "No", "No internet service"])

OnlineBackup = st.selectbox("OnlineBackup", ["Yes", "No", "No internet service"])

DeviceProtection = st.selectbox("DeviceProtection", ["Yes", "No", "No internet service"])

TechSupport = st.selectbox("TechSupport", ["Yes", "No", "No internet service"])

StreamingTV = st.selectbox("StreamingTV", ["Yes", "No", "No internet service"])

StreamingMovies = st.selectbox("StreamingMovies", ["Yes", "No", "No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

PaperlessBilling = st.selectbox("PaperlessBilling", ["Yes", "No"])

PaymentMethod = st.selectbox("PaymentMethod", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

MonthlyCharges = st.number_input("MonthlyCharges", value=0.0, step=1.0, min_value=0.0)

TotalCharges = st.number_input("TotalCharges", value=0.0, step=1.0, min_value=0.0)

user_data = pd.DataFrame([[
    gender, SeniorCitizen, Partner, Dependents, tenure,
    PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
    DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
    PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges
]], columns=[
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"
])

if st.button("Predict"):   
    user_input = [
        gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines,
        InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
        StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges
        ]
    prediction = model.predict(user_data)[0]

    if prediction == 'Yes':
        st.error("❌ Customer is likely to churn.")
    else:
        st.success("✅ Customer is not likely to churn.")