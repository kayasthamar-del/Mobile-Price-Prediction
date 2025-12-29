import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

st.title("📱 Mobile Phone Price Prediction App")

# Load data
data = pd.read_csv("mobile_data.csv")

X = data.drop("price_range", axis=1)
y = data["price_range"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

st.write("Enter mobile phone details:")

ram = st.number_input("RAM (GB)", 1, 16)
storage = st.number_input("Storage (GB)", 8, 256)
battery = st.number_input("Battery (mAh)", 2000, 6000)
camera = st.number_input("Camera (MP)", 5, 108)

if st.button("Predict Price"):
    input_data = np.array([[ram, storage, battery, camera]])
    prediction = model.predict(input_data)

    if predicted_price < 15000:
              range_label = "Low"
elif predicted_price < 25000:
    range_label = "Medium"
elif predicted_price < 40000:
    range_label = "High"
else:
    range_label = "Premium"



