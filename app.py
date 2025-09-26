import streamlit as st
import pickle
import numpy as np
import os

# Load the model
model_path = os.path.join("assets", "model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏠 House Price Prediction App")

st.markdown("Enter the details below to predict the **house price**:")

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10)
area = st.number_input("Area (sqft)", min_value=200, max_value=10000 )
location_score = st.slider("Location Score", min_value=1, max_value=10 )
age = st.number_input("Age of House (years)", min_value=0, max_value=100)

# Prediction button
if st.button("Predict Price"):
    features = np.array([[bedrooms, bathrooms, area, location_score, age]])
    prediction = model.predict(features)

    # Show predicted price
    st.success(f"💰 Estimated Price: ${prediction[0]:,.2f}")

    # Disclaimer in a styled box
    st.info("⚠️ These are estimated predictions based on the model. "
            "Actual market prices may vary due to other factors.")

# Footer - always at bottom, centered
st.markdown(
    """
    <br><br><hr>
    <div style="text-align: center; color: grey; font-size: 14px;">
        ✅ Developed by <b>Amna Talha</b>
    </div>
    """,
    unsafe_allow_html=True
)
