import random
import yfinance as yf
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator


def get_signal(symbol, timeframe):
    try:
        tf = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1H": "60m",
            "60m": "60m"
        }.get(timeframe, "5m")

        data = yf.download(
            symbol,
            period="5d",
            interval=tf,
            progress=False,
            auto_adjust=False
        )

        if data.empty:
            return "NO SIGNAL", 0

        close = data["Close"].squeeze()

        ema8 = EMAIndicator(close, window=8).ema_indicator()
        ema21 = EMAIndicator(close, window=21).ema_indicator()
        rsi = RSIIndicator(close, window=14).rsi()

        buy = 0
        sell = 0

        if ema8.iloc[-1] > ema21.iloc[-1]:
            buy += 60
        else:
            sell += 60

        if rsi.iloc[-1] > 55:
            buy += 40
        elif rsi.iloc[-1] < 45:
            sell += 40

        if buy > sell:
            return "BUY", min(99, buy + random.randint(0, 5))
        elif sell > buy:
            return "SELL", min(99, sell + random.randint(0, 5))
        else:
            return "NO SIGNAL", 0

    except Exception as e:
        print(e)
        return "NO SIGNAL", 0
