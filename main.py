import xgboost as xgb
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("my_random_forest.joblib")

@st.cache

def predict(o, n, s, c):
    return model.predict([[o,n,s,c]])

st.title('AQI Prediction')
st.header('Enter the values:')

o = st.number_input('O3')
n = st.number_input('NO2')
s = st.number_input('SO2')
c = st.number_input('CO')

if st.button('Predict AQI'):
    AQI = predict(o,n,s,c)
    st.success(f'AQI {AQI[0]:.2f}')