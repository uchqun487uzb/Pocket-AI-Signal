from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from backend.trading_signal import get_signal

TOKEN = "8703489111:AAEdKRhWlvf--inlKzUgb8KTMiEj-Z2WSlI"

keyboard = ReplyKeyboardMarkup(
    [
        ["1 daqiqa", "5 daqiqa"],
        ["15 daqiqa", "30 daqiqa"],
        ["1 soat"],
    ],
    resize_keyboard=True,
)

pair = "EURUSD=X"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Uchqun.S AI\n\nTimeframe tanlang:",
        reply_markup=keyboard,
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1 daqiqa":
        tf = "1m"
    elif text == "5 daqiqa":
        tf = "5m"
    elif text == "15 daqiqa":
        tf = "15m"
    elif text == "30 daqiqa":
        tf = "30m"
    elif text == "1 soat":
        tf = "60m"
    else:
        return

    sig, conf = get_signal(pair, tf)

    if sig == "BUY":
        emoji = "🟢"
    elif sig == "SELL":
        emoji = "🔴"
    else:
        emoji = "⚪"

    msg = f"""
🤖 Uchqun.S AI

━━━━━━━━━━━━━━

{emoji} {sig}

💱 EUR/USD
⏰ {tf}

🎯 Ishonchlilik: {conf}%

━━━━━━━━━━━━━━

⚠️ Riskni boshqarishni unutmang.
"""

    await update.message.reply_text(msg)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, signal))

    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
