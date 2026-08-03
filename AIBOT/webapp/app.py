from flask import Flask, render_template, request, jsonify
import sys

sys.path.append("../backend")
from trading_signal import get_signal

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signal")
def signal():
    symbol = request.args.get("symbol", "EURUSD")
    timeframe = request.args.get("timeframe", "1m")

    signal, confidence = get_signal(symbol, timeframe)

    return jsonify({
        "signal": signal,
        "confidence": confidence
    })


@app.route("/pairs")
def pairs():
    forex = [
        "EURUSD","GBPUSD","USDJPY","AUDUSD","NZDUSD",
        "USDCAD","USDCHF","EURJPY","GBPJPY","EURGBP",
        "AUDCAD","AUDJPY","AUDCHF","CADJPY","CHFJPY",
        "EURAUD","EURCAD","EURCHF","GBPAUD","GBPCAD",
        "GBPCHF","NZDCAD","NZDCHF","NZDJPY","CADCHF",
        "EURNZD","GBPNZD","AUDNZD","USDMXN","USDSEK",
        "USDNOK","USDSGD","EURSEK","EURNOK","GBPSEK",
        "XAUUSD","XAGUSD","BTCUSD","ETHUSD"
    ]

    otc = [
        "EURUSD OTC","GBPUSD OTC","USDJPY OTC","AUDUSD OTC",
        "NZDUSD OTC","USDCAD OTC","USDCHF OTC","EURJPY OTC",
        "GBPJPY OTC","EURGBP OTC","AUDCAD OTC","AUDJPY OTC",
        "AUDCHF OTC","CADJPY OTC","CHFJPY OTC","EURAUD OTC",
        "EURCAD OTC","EURCHF OTC","GBPAUD OTC","GBPCAD OTC",
        "GBPCHF OTC","NZDCAD OTC","NZDCHF OTC","NZDJPY OTC",
        "CADCHF OTC","EURNZD OTC","GBPNZD OTC","AUDNZD OTC",
        "AEDCNY OTC","USDPKR OTC","USDTRY OTC","EURTRY OTC",
        "GBPTRY OTC","USDBRL OTC","USDARS OTC","USDINR OTC",
        "USDIDR OTC","USDPHP OTC","EURUSD OTC 2","GBPUSD OTC 2"
    ]

    return jsonify({
        "forex": forex,
        "otc": otc
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
