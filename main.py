import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components

model = joblib.load("my_random_forest.joblib")

@st.cache

def predict(o, n, s, c):
    return model.predict([[o,n,s,c]])

st.title('AQI Prediction')
HtmlFile = open("./index.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=300)
st.header('Enter the values:')
st.write("As current script is not crawling data automatically, I added widget to get data")
o = st.number_input('O3')
n = st.number_input('NO2')
s = st.number_input('SO2')
c = st.number_input('CO')

if st.button('Predict AQI'):
    AQI = predict(o,n,s,c)
    st.success(f'AQI {AQI[0]:.2f}')