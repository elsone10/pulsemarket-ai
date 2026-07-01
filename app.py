import streamlit as st
import requests

st.title("PulseMarket: Full Meme Data")

def get_data():
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get('pairs', [])
        return None
    except:
        return None

if st.button("Get Full Token Data"):
    with st.spinner('Fetching...'):
        tokens = get_data()
        if tokens:
            for t in tokens[:5]:
                info = t.get('info', {})
                socials = info.get('socials', [])
                twitter = next((s['url'] for s in socials if s['type'] == 'twitter'), "No Twitter")
                
                st.write(f"### {t.get('baseToken', {}).get('symbol')}")
                st.write(f"**Price:** ${t.get('priceUsd')}")
                st.write(f"**Liquidity:** ${t.get('liquidity', {}).get('usd', 0):,.2f}")
                st.write(f"**Twitter:** {twitter}")
                st.markdown("---")
        else:
            st.error("Server block detected. Please refresh or try again.")
