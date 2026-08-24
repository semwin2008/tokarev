from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from model.model_interface import get_model_reply


async def start(update: Update, context):
    await update.message.reply_text("Я лох")


async def reply(update: Update, context):
    input_text = update.message.text[8:]
    print(f'model query, message is: {input_text}')
    reply = get_model_reply(input_text)
    await update.message.reply_text(reply)


if __name__ == "__main__":
    # I assume that this file contains telegram bot token
    with open('.env/TOKEN', 'r', encoding='utf-8') as file:
        TOKEN = file.readline().strip()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'tokarev +'), reply))
    app.run_polling()
