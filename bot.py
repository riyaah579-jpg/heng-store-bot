import os
import requests
from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Top Up", callback_data="topup")],
        [InlineKeyboardButton("💎 Price List", callback_data="prices")],
        [InlineKeyboardButton("📦 Check Order", callback_data="check")],
        [InlineKeyboardButton("📞 Contact Admin", callback_data="contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎉 Welcome to Heng Store\n\nChoose a menu:",
        reply_markup=reply_markup,
    )(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🎮 Available Games

🔥 Free Fire
🔥 Mobile Legends
🔥 PUBG Mobile
"""
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("games", games))

# Add this line below the CommandHandlers
app.add_handler(CallbackQueryHandler(button))


import asyncio

async def main():
    print("Bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
