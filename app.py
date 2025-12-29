import streamlit as st
import pickle
import numpy as np

st.title("📱 Mobile Price Prediction App")

st.write("Enter mobile phone details below:")

ram = st.number_input("RAM (GB)", 1, 16)
storage = st.number_input("Storage (GB)", 8, 256)
battery = st.number_input("Battery (mAh)", 2000, 6000)
camera = st.number_input("Camera (MP)", 5, 108)

if st.button("Predict Price"):
    st.write("Prediction will appear here")
