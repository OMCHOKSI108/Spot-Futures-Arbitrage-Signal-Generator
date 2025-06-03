import requests
from bs4 import BeautifulSoup

def get_risk_free_rate():
    try:
        response = requests.get("https://rbi.org.in")
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        if "91-Day T-Bill" in text:
            idx = text.index("91-Day T-Bill")
            value = text[idx:idx+100].split("%")[0].split()[-1]
            return float(value)/100
    except:
        pass
    return 0.0835