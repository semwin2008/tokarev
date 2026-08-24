from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


async def start(update: Update, context):
    await update.message.reply_text("Привет!")


async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)



if __name__ == "__main__":
    # I assume that this file contains telegram bot token
    with open('.env/TOKEN', 'r', encoding='utf-8') as file:
        TOKEN = file.readline().strip()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()
