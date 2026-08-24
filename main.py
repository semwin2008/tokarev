import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TimedOut, NetworkError
from model.model_interface import get_model_reply


async def start(update: Update, context):
    await update.message.reply_text("Я лох")


async def reply(update: Update, context):
    input_text = update.message.text[8:]
    print(f'model query, message is: {input_text}')
    
    try:
        reply_text = await asyncio.to_thread(get_model_reply, input_text)
        
        await update.message.reply_text(reply_text, read_timeout=30, write_timeout=30)
        
    except Exception as e:
        print(f"Error in reply handler: {e}")
        await update.message.reply_text('Произошел наеп...')


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает ошибки"""
    if isinstance(context.error, TimedOut):
        print("Timed out error occurred")
        if hasattr(update, 'message') and update.message:
            try:
                await update.message.reply_text('Бож, сервер не отвечает(')
            except:
                pass
    else:
        print(f"Unhandled error: {context.error}")


if __name__ == "__main__":
    with open('.env/TOKEN', 'r', encoding='utf-8') as file:
        TOKEN = file.readline().strip()
    
    # Увеличиваем таймауты для всего приложения
    app = Application.builder() \
        .token(TOKEN) \
        .read_timeout(30) \
        .write_timeout(30) \
        .connect_timeout(30) \
        .pool_timeout(30) \
        .build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'tokarev +'), reply))
    
    # Регистрируем обработчик ошибок
    app.add_error_handler(error_handler)
    
    print("Бот запущен...")
    app.run_polling()