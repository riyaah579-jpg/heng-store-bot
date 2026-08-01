import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🎮 Welcome to Heng Store

💎 Game Top Up Bot

Commands:

/games - View games
/price - View prices
/order - Create order
"""
    )


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🎮 Available Games

🔥 Free Fire
🔥 Mobile Legends
🔥 PUBG Mobile
"""
    )


app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("games", games)
)


print("Bot is running...")

app.run_polling()
