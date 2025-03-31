
import streamlit as st
import requests

st.title("💱 Currency Converter")

# Get Exchange Rates
api_url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(api_url)
data = response.json()
currencies = list(data["rates"].keys())

# User Inputs
from_currency = st.selectbox("From Currency:", currencies)
to_currency = st.selectbox("To Currency:", currencies)
amount = st.number_input("Amount:", min_value=0.01, format="%.2f")

# Convert
if st.button("Convert"):
    rate = data["rates"][to_currency] / data["rates"][from_currency]
    converted_amount = round(amount * rate, 2)
    st.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")

