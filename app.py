import streamlit as st
import requests

st.title("PulseMarket: Alpha Scanner")

def get_birdeye_data():
    # Amfani da API na Birdeye wanda ya fi karfin toshewa
    url = "https://public-api.birdeye.so/defi/token_trending?sort_by=rank&sort_type=desc&limit=10&offset=0"
    headers = {
        "x-chain": "solana",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('data', {}).get('tokens', [])
        return None
    except:
        return None

if st.button("Scan Alpha"):
    with st.spinner('Fetching Alpha...'):
        tokens = get_birdeye_data()
        if tokens:
            st.success("Alpha Data Fetched!")
            for t in tokens:
                st.write(f"### {t.get('symbol')}")
                st.write(f"Price: ${t.get('price', 0):.6f}")
                st.write(f"24h Vol: ${t.get('volume24hUSD', 0):,.2f}")
                st.markdown("---")
        else:
            st.error("Birdeye error. Check your connection or API status.")
