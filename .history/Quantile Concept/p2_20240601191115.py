import logging
from telegram.ext import Updater, CommandHandler
import asyncio
import threading

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram API credentials
API_ID = '24158657'
API_HASH = '1b7b03ef18268334aaadf7ae1097bba1'
SOURCE_CHANNEL = 'https://t.me/gapup_channel_official'

# Telegram bot token
TELEGRAM_BOT_TOKEN = '7204627673:AAHYqjBSQTcyiSvXU2Od-NwvfEY4dRJcaPk'
DESTINATION_CHANNEL_ID = '@rupesh_alert'  # Replace with the actual username of your destination channel

# Initialize the Telegram bot
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

async def forward_message_to_channel(update, context):
    message = update.message.text
    # Define your filter condition here
    if 'Message by : SAURABH SAHU' in message:  # Replace 'your keyword' with the actual keyword
        await context.bot.send_message(chat_id=DESTINATION_CHANNEL_ID, text=message)

def start(update, context):
    update.message.reply_text('Bot started!')

# Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("forward", forward_message_to_channel))

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
