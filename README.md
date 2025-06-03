# 📈 Spot-Futures Arbitrage Signal System

This project identifies **arbitrage opportunities** between the **spot and futures prices** of stocks and indices based on the cost-of-carry model. If the spread between the futures market price and the fair value exceeds a threshold, the system provides a **Buy Spot / Sell Futures** or **Sell Spot / Buy Futures** signal.

---

## 🧠 Core Formula

Fair Value (Futures) = Spot Price × [1 + (rf × x / 365)] – d

Where:
- `rf`: Risk-free interest rate (auto-fetched from RBI or fixed at fallback 8.35%)
- `x`: Number of days to expiry
- `d`: Expected dividend

---

## 🛠️ Features

- 📡 Live spot price fetch for **stocks and indices** via Yahoo Finance (`yfinance`)
- 📉 Futures price simulated or fetchable via NSE (extendable)
- 🔄 Auto fetches **91-day T-Bill yield** from RBI website
- ✅ Streamlit frontend for live trade signals
- 🚀 FastAPI backend API for calculation logic
- 📦 Modular backend utility structure
- 🔔 Live arbitrage signal if spread > threshold

---

## 🖥️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit
- **Data Source**: `yfinance`, RBI site
- **Other Tools**: BeautifulSoup, Requests, CORS

---

## 📂 Folder Structure
spot-futures-arbitrage/

├── backend/

  ├── app.py

├──utils/

  ├── fair_value.py
  
  ├── scraper_rbi.py
  
  └── nse_fetcher.py
  
├── frontend/

  └── streamlit_app.py
  
├── requirements.txt

