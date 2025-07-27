import os
import time
import requests
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Telegram config
TELEGRAM_TOKEN = "8034746391:AAFEi1HrMNdDS3jLX8mFGz5vWjR7K1Aw3LY"
CHAT_ID = "5573886497"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    ticker = data.get("ticker", "Unknown")
    action = data.get("action", "No action provided")
    message = f"📈 {ticker} Alert!\nAction: {action}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    send_telegram_message(message)
    return "Alert received", 200

if __name__ == "__main__":
    app.run(debug=True)
