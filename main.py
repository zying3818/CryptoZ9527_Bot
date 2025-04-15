
import os
from telegram.ext import ApplicationBuilder, CommandHandler
import openai

# 初始化 Telegram bot
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

async def start(update, context):
    await update.message.reply_text("欢迎使用 CryptoZ9527 Bot！")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
