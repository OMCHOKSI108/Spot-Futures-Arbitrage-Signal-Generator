import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("📊 Spot-Futures Arbitrage Signal Generator")

symbols = ["RELIANCE", "TCS", "INFY", "WIPRO", "NIFTY", "BANKNIFTY", "HDFCBANK", "ICICIBANK", "ITC", "LT", "SBIN"]
symbol = st.selectbox("Select Stock/Index Symbol", symbols)
expiry_days = st.slider("Days to Expiry", 1, 90, 30)
dividend = st.number_input("Dividend (₹)", min_value=0.0, value=0.0)
threshold = st.number_input("Min Spread to Trigger Signal (₹)", value=5.0)

if st.button("Check Arbitrage Opportunity"):
    with st.spinner("Fetching Data & Calculating..."):
        response = requests.post("http://localhost:8000/check-arbitrage", json={
            "symbol": symbol,
            "expiry_days": expiry_days,
            "dividend": dividend,
            "threshold": threshold
        })
        if response.status_code == 200:
            data = response.json()
            st.metric("Spot Price", f"₹{data['spot_price']}")
            st.metric("Futures Price", f"₹{data['future_price']}")
            st.metric("Fair Value", f"₹{data['fair_value']}")
            st.metric("Spread", f"₹{data['spread']}")
            st.success(f"🔔 Signal: {data['signal']}")
        else:
            st.error("Error fetching data")