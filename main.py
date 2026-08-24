from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from model.model_interface import get_model_reply


async def start(update: Update, context):
    await update.message.reply_text("Я лох")


async def reply(update: Update, context):
    reply = get_model_reply(update.message.text)
    await update.message.reply_text(reply)


if __name__ == "__main__":
    # I assume that this file contains telegram bot token
    with open('.env/TOKEN', 'r', encoding='utf-8') as file:
        TOKEN = file.readline().strip()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Mention, reply))
    app.run_polling()
