import streamlit as st
import requests

st.title("PulseMarket AI Scanner")

def get_real_solana_data():
    # URL ɗin da ya fi dacewa don kamo bayanai
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('pairs', [])[:5]
        return None
    except Exception as e:
        return None

if st.button("Scan Market"):
    with st.spinner('Scanning...'):
        tokens = get_real_solana_data()
        if tokens and len(tokens) > 0:
            st.success("Analysis Complete!")
            for token in tokens:
                symbol = token.get('baseToken', {}).get('symbol', 'N/A')
                price = token.get('priceUsd', 'N/A')
                st.write(f"**{symbol}**: ${price}")
        else:
            st.warning("No data found or connection issue. Please try again.")
