import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Telegram Bot Token
BOT_TOKEN = "8196519066:AAGwl-4GYirVvh8IneNJs3qxVwQXs599zlA"

# Panel API URL
API_URL = "https://api.temporasms.com/stubs/handler_api.php?api_key=8d327e852edef6ea97e9b42788edeebaaf07&action=getNumberV2&service=itvh&country=12&operator=9&maxPrice=1.0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Number bhejo.\nExample:\n9876543210"
    )

async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()

    if not number.isdigit():
        await update.message.reply_text("Sirf number bhejo.")
        return

    payload = {
        "number": number,
        "apikey": "8d327e852edef6ea97e9b42788edeebaaf07"
    }

    try:
        response = requests.post(API_URL, data=payload, timeout=20)

        if response.status_code == 200:
            await update.message.reply_text(
                f"API Response:\n{response.text}"
            )
        else:
            await update.message.reply_text(
                f"Error: {response.status_code}"
            )

    except Exception as e:
        await update.message.reply_text(str(e))

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

    print("Bot Started...")
    app.run_polling()
