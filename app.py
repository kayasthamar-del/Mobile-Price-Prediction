import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("📱 Mobile Phone Price Prediction App")

# Load dataset
data = pd.read_csv("mobile_data.csv")

X = data.drop("price_range", axis=1)
y = data["price_range"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

st.subheader("Enter Mobile Specifications")

ram = st.number_input("RAM (GB)", 1, 16, 1)
storage = st.number_input("Storage (GB)", 8, 256, 8)
battery = st.number_input("Battery (mAh)", 2000, 6000, 100)
camera = st.number_input("Camera (MP)", 5, 108, 1)

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "ram": [ram],
        "storage": [storage],
        "battery": [battery],
        "camera": [camera]
    })

    predicted_class = model.predict(input_data)[0]

    if predicted_class == 0:
        label = "Low"
    elif predicted_class == 1:
        label = "Medium"
    elif predicted_class == 2:
        label = "High"
    else:
        label = "Premium"

    st.success(f"Predicted Price Category: {label}")
