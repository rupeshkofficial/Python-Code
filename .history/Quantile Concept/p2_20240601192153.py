import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update
import asyncio
import threading

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TELEGRAM_BOT_TOKEN = '7204627673:AAHYqjBSQTcyiSvXU2Od-NwvfEY4dRJcaPk'

# Initialize the updater
updater = Updater(token=TELEGRAM_BOT_TOKEN)
dispatcher = updater.dispatcher

async def forward_message_to_channel(update: Update, context):
    message = update.message.text
    # Define your filter condition here
    if 'Message by : SAURABH SAHU' in message:  # Replace 'your keyword' with the actual keyword
        await context.bot.send_message(chat_id='@rupesh_alert', text=message)

def start(update: Update, context):
    update.message.reply_text('Bot started!')

# Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(None, forward_message_to_channel))

def start_bot():
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    # Start the bot in a new thread
    threading.Thread(target=start_bot).start()

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    finally:
        loop.close()
