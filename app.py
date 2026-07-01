import streamlit as st
import requests

st.title("PulseMarket: Direct Scanner")

def get_solscan_data():
    # Amfani da Public Endpoint na Solscan
    url = "https://public-api.solscan.io/token/market?tokenAddress=So11111111111111111111111111111111111111112"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

if st.button("Scan Now"):
    data = get_solscan_data()
    if data:
        st.write("### Market Data")
        st.write(f"Price: ${data.get('priceUsd', 0)}")
        st.write(f"Volume: ${data.get('volume24h', 0):,.2f}")
    else:
        st.error("Scanner active. Please wait 1 minute and try again.")
