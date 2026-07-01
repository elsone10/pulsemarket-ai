import streamlit as st
import requests

st.title("PulseMarket AI Scanner")

def get_data():
    # Amfani da API daban wanda ya fi buɗe kofa
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    headers = {"User-Agent": "Mozilla/5.0"} # Wannan yana sa a ɗauke mu a matsayin mai amfani da browser
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('pairs', [])[:5]
        return None
    except:
        return None

if st.button("Scan Market"):
    with st.spinner('Scanning...'):
        tokens = get_data()
        if tokens:
            for token in tokens:
                symbol = token.get('baseToken', {}).get('symbol', 'N/A')
                price = token.get('priceUsd', 'N/A')
                st.write(f"**{symbol}**: ${price}")
        else:
            st.error("Cannot reach server. Try checking your network.")
