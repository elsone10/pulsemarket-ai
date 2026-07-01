import streamlit as st
import requests

st.title("PulseMarket AI Scanner")

def get_real_solana_data():
    # Amfani da API na DexScreener don kamo bayanan gaske
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Muna tace bayanan su zama gajeru
            return data.get('pairs', [])[:5]
        return None
    except:
        return None

if st.button("Scan Market"):
    with st.spinner('Fetching real Solana data...'):
        tokens = get_real_solana_data()
        if tokens:
            st.success("Analysis Complete!")
            for token in tokens:
                st.write(f"**Token**: {token['baseToken']['symbol']} | **Price**: ${token['priceUsd']}")
        else:
            st.error("Failed to fetch real data.")
