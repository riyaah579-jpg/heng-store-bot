import os
import asyncio
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


# =========================
# START COMMAND
# =========================
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
    )


# =========================
# GAMES COMMAND
# =========================
async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🎮 Available Games

🔥 Free Fire
⚔️ Mobile Legends
🏆 PUBG Mobile
"""
    )


# =========================
# BUTTON HANDLER
# =========================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "topup":
        await query.edit_message_text(
            "🎮 Choose a game:\n\n🔥 Free Fire\n⚔️ Mobile Legends\n🏆 PUBG Mobile"
        )

    elif query.data == "prices":
        await query.edit_message_text(
            "💎 Price List\n\nComing soon..."
        )

    elif query.data == "check":
        await query.edit_message_text(
            "📦 Send your Order ID."
        )

    elif query.data == "contact":
        await query.edit_message_text(
            "📞 Contact Admin\n@YourUsername"
        )


# =========================
# CREATE APP
# =========================
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("games", games))
app.add_handler(CallbackQueryHandler(button))


# =========================
# MAIN
# =========================
async def main():
    print("Bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
