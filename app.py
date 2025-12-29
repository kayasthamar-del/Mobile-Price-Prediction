import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(page_title="Mobile Price Prediction", layout="centered")

st.title("📱 Mobile Phone Price Prediction App")

# Load dataset
data = pd.read_csv("mobile_data.csv")

X = data.drop("price_range", axis=1)
y = data["price_range"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

st.subheader("Enter Mobile Specifications")

ram = st.number_input("RAM (GB)", min_value=1, max_value=16, step=1)
storage = st.number_input("Storage (GB)", min_value=8, max_value=256, step=8)
battery = st.number_input("Battery (mAh)", min_value=2000, max_value=6000, step=100)
camera = st.number_input("Camera (MP)", min_value=5, max_value=108, step=1)

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "ram": [ram],
        "storage": [storage],
        "battery": [battery],
        "camera": [camera]
    })

    predicted_class = model.predict(input_data)[0]

    if predicted_class == 0:
        range_label = "Low"
    elif predicted_class == 1:
        range_label = "Medium"
    elif predicted_class == 2:
        range_label = "High"
    else:
        range_label = "Premium"

    st.success(f"📊 Predicted Price Category: **{range_label}**")
