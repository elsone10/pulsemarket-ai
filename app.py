import streamlit as st
import requests

st.title("PulseMarket: Full Meme Data")

def get_full_meme_data():
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('pairs', [])
        return []
    except:
        return []

if st.button("Get Full Token Data"):
    tokens = get_full_meme_data()
    if tokens:
        for t in tokens[:5]:
            info = t.get('info', {})
            socials = info.get('socials', [])
            twitter = next((s['url'] for s in socials if s['type'] == 'twitter'), "No Twitter")
            
            # Cikakken bayanin coin
            st.write(f"### {t.get('baseToken', {}).get('symbol')}")
            st.write(f"**Price:** ${t.get('priceUsd')}")
            st.write(f"**Liquidity:** ${t.get('liquidity', {}).get('usd', 0):,.2f}")
            st.write(f"**24h Vol:** ${t.get('volume', {}).get('h24', 0):,.2f}")
            st.write(f"**Twitter:** {twitter}")
            st.write(f"**DEX ID:** {t.get('dexId')}")
            st.markdown("---")
    else:
        st.error("Cannot fetch full data.")
