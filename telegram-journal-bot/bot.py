import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "http://127.0.0.1:8000/analyze"
SHEET_ID = "1uLcaiGGW90b2xueGEYmyjol8jl3zVBuqpvZ9XMTrzTE"


def get_sheet_summary():
    resp = requests.post(
        API_URL,
        json={"sheet_id": SHEET_ID, "range": "A1:U10"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["summary"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я дневниковый бот.\nНапиши /summary, чтобы получить краткий анализ записей."
    )


async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Думаю над записями, подожди пару секунд...")
    try:
        summary_text = get_sheet_summary()
        await update.message.reply_text(summary_text[:4000])
    except Exception as e:
        await update.message.reply_text(f"Ошибка при анализе: {e}")


def main():
    if not TELEGRAM_TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN is not set")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("summary", summary))

    app.run_polling()


if __name__ == "__main__":
    main()

