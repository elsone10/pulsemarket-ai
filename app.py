import streamlit as st
import requests
import time

st.title("PulseMarket: Anti-Block Scanner")

# Wannan zai ba da damar sake gwadawa sau 3 idan ya kasa (Retry mechanism)
def get_data():
    url = "https://api.dexscreener.com/latest/dex/search?q=solana"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    for i in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json().get('pairs', [])
            time.sleep(2) # Jira kadan idan ya kasa
        except:
            continue
    return None

if st.button("Scan Market"):
    tokens = get_data()
    if tokens:
        for t in tokens[:5]:
            symbol = t.get('baseToken', {}).get('symbol')
            st.write(f"**{symbol}**: ${t.get('priceUsd')}")
    else:
        st.error("Duk hanyoyin sun gaza. Bari mu gwada wani API na daban.")
