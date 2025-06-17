import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}


session = requests.Session()
session.headers.update(headers)

def get_spot_price(symbol):
    try:
        session.get("https://www.nseindia.com", timeout=5)  # get cookies
        url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol.upper()}"
        res = session.get(url, timeout=5)
        data = res.json()
        return float(data["priceInfo"]["lastPrice"])
    except Exception as e:
        print("Spot fetch error:", e)
        return 0.0

def get_futures_price(symbol):
    try:
        time.sleep(1)  # delay for server
        url = f"https://www.nseindia.com/api/quote-derivative?symbol={symbol.upper()}"
        res = session.get(url, timeout=5)
        data = res.json()
        # First expiry contract
        return float(data["stocks"][0]["marketDeptOrderBook"]["tradeInfo"]["lastPrice"])
    except Exception as e:
        print("Futures fetch error:", e)
        return 0.0

def get_spot_and_futures_price(symbol):
    spot = get_spot_price(symbol)
    future = get_futures_price(symbol)
    return spot, future
