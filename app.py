import streamlit as st
import requests

st.title("PulseMarket: Integrity Scanner")

def analyze_token(token_data):
    score = 0
    liquidity = token_data.get('liquidity', {}).get('usd', 0)
    if liquidity > 10000:
        score += 50
    socials = token_data.get('info', {}).get('socials', [])
    twitter = any(s['type'] == 'twitter' for s in socials)
    if twitter:
        score += 30
    return score

def get_solana_pairs():
    url = "https://api.dexscreener.com/latest/dex/search?q=solana"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('pairs', [])
        return []
    except:
        return []

if st.button("Scan Integrity"):
    tokens = get_solana_pairs()
    found = False
    for t in tokens:
        score = analyze_token(t)
        if score >= 80:
            st.write(f"**Alpha Detected**: {t['baseToken']['symbol']} | **Score**: {score}")
            st.write(f"**Price**: ${t['priceUsd']}")
            st.write("---")
            found = True
    if not found:
        st.write("No high-integrity tokens found.")
