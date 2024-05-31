import time
import psutil
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7064127939:AAG0FBroVf-5MulztyTbrtenYM6UimGv3GA'
CHAT_ID = '1366563572'

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    return cpu_percent, ram_percent

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="CPU and RAM Monitoring Started.")
    while True:
        cpu_percent, ram_percent = get_system_info()
        if ram_percent > 50:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"High Resource Usage Detected:\nRAM Usage: {ram_percent}%"
            )
        if cpu_percent > 50:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"High Resource Usage Detected:\nCPU Usage: {cpu_percent}"
            )
        time.sleep(5)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
