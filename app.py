import streamlit as st
import pickle
import numpy as np
import os
import matplotlib.pyplot as plt

# Load the model
model_path = os.path.join("assets", "model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏠 House Price Prediction App")

st.markdown("Enter the details below to predict the **house price**:")

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=1)
area = st.number_input("Area (sqft)", min_value=200, max_value=10000, value=1200)
location_score = st.slider("Location Score", min_value=1, max_value=10, value=5)
age = st.number_input("Age of House (years)", min_value=0, max_value=100, value=5)

# Prediction button
if st.button("Predict Price"):
    features = np.array([[bedrooms, bathrooms, area, location_score, age]])
    prediction = model.predict(features)
    st.success(f"💰 Estimated Price: ${prediction[0]:,.2f}")

    # # Visualization panel
    # st.subheader("📊 Input Summary")
    # labels = ["Bedrooms", "Bathrooms", "Area_sqft", "Location_Score", "Age_years"]
    # values = [bedrooms, bathrooms, area, location_score, age]

    # fig, ax = plt.subplots(figsize=(6,4))
    # ax.bar(labels, values, color="skyblue", edgecolor="black")
    # ax.set_title("User Inputs Overview")
    # ax.set_ylabel("Values")
    # plt.xticks(rotation=30)
    #
    # st.pyplot(fig)
