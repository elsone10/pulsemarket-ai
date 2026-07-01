import streamlit as st
import requests

st.title("PulseMarket: Integrity Scanner")

def get_data():
    # Amfani da wani API proxy don kaucewa toshewa
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    # Muna amfani da header wanda ya fi kama da na gaske
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        # Kara wani proxy layer idan kana da shi, amma fara da wannan
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get('pairs', [])
        return None
    except:
        return None

if st.button("Get Full Token Data"):
    with st.spinner('Loading data...'):
        tokens = get_data()
        if tokens:
            st.success("Data Fetched Successfully!")
            for t in tokens[:5]:
                symbol = t.get('baseToken', {}).get('symbol', 'N/A')
                price = t.get('priceUsd', '0')
                liq = t.get('liquidity', {}).get('usd', 0)
                st.write(f"### {symbol}")
                st.write(f"Price: ${price} | Liq: ${liq:,.2f}")
                st.markdown("---")
        else:
            st.error("Still blocked. Please try to 'Reboot' the app from Manage app menu.")
