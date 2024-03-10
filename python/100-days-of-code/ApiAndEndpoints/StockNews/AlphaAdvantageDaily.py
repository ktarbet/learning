from datetime import datetime,timedelta, date

import requests
import os

STOCK_ENDPOINT = "https://www.alphavantage.co/query"


class AlphaAdvantageDaily:

    def __init__(self, stock):
        self.stock = stock
        args = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock,
            "apikey": os.environ.get("API_KEY")
        }
        # "https://www.alphavantage.co/query?&symbol=IBM&apikey=demo"
        response = requests.get(STOCK_ENDPOINT, args)
        response.raise_for_status()

        self.data = response.json()
        self.time_series = self.data['Time Series (Daily)']

    def percent_increase(self):
        t = date.today()
        t0 = t - timedelta(days=1)
        # 2024-03-05
        t = str(t)
        t0 = str(t0)
        ts = self.time_series
        if t in ts and t0 in ts:
            p0 = float(ts[t0]["4. close"])
            p = float(ts[t]["4. close"])
            percent_change = 100.0*(p - p0)/p0
            return percent_change
        return None
