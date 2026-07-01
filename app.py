import streamlit as st
import requests

st.title("PulseMarket AI Scanner")

@st.cache_data(ttl=30)
def get_data():
    url = "https://api.dexscreener.com/latest/dex/search?q=solana"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json().get('pairs', [])[:5]
    except:
        return None
    return None

if st.button("Scan Market"):
    with st.spinner('Scanning...'):
        tokens = get_data()
        if tokens:
            for token in tokens:
                st.write(f"**{token.get('baseToken', {}).get('symbol')}**: ${token.get('priceUsd')}")
        else:
            st.error("Connection failed. Try refreshing the page.")
