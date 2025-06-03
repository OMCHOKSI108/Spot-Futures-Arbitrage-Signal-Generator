from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.fair_value import calculate_fair_value
from utils.nse_fetcher import get_spot_and_futures_price
from utils.scraper_rbi import get_risk_free_rate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ArbitrageInput(BaseModel):
    symbol: str
    expiry_days: int
    dividend: float = 0
    threshold: float = 5.0

@app.post("/check-arbitrage")
def check_arbitrage(data: ArbitrageInput):
    spot, future = get_spot_and_futures_price(data.symbol)
    rf = get_risk_free_rate()
    fv = calculate_fair_value(spot, rf, data.expiry_days, data.dividend)
    spread = future - fv

    if abs(spread) >= data.threshold:
        signal = "Buy Spot, Sell Futures" if spread > 0 else "Sell Spot, Buy Futures"
    else:
        signal = "No Trade"

    return {
        "spot_price": spot,
        "future_price": future,
        "fair_value": round(fv, 2),
        "spread": round(spread, 2),
        "signal": signal
    }