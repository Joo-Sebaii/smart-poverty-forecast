import streamlit as st
import requests

st.set_page_config(page_title="Smart Poverty Forecast")

st.title("📊 Smart Poverty Forecast")

API_URL = "http://127.0.0.1:8000/predict"

income = st.number_input("Current Income (median_household_income):", 0.0)
poverty_last_year = st.number_input("Poverty Last Year (%):", 0.0)
income_last_year = st.number_input("Income Last Year:", 0.0)
avg_3yr = st.number_input("3-Year Poverty Average (%):", 0.0)

if st.button("Predict Poverty Levels"):
    params = {
        "income": income,
        "poverty_last_year": poverty_last_year,
        "income_last_year": income_last_year,
        "avg_3yr": avg_3yr,
    }

    response = requests.post(API_URL, params=params)

    if response.status_code == 200:
        result = response.json()

        st.success("Prediction Complete")
        st.write("### Poverty All Ages Prediction:")
        st.write(f"🔹 **{result['poverty_all_prediction']:.2f}%**")

        st.write("### Poverty Under 18 Prediction:")
        st.write(f"🔹 **{result['poverty_under18_prediction']:.2f}%**")
    else:
        st.error("Error: Could not contact the API")
