import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import asyncio
import threading

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TELEGRAM_BOT_TOKEN = '7204627673:AAHYqjBSQTcyiSvXU2Od-NwvfEY4dRJcaPk'

def forward_message_to_channel(update, context):
    message = update.message.text
    # Define your filter condition here
    if 'Message by : SAURABH SAHU' in message:  # Replace 'your keyword' with the actual keyword
        context.bot.send_message(chat_id='@rupesh_alert', text=message)

def start(update, context):
    update.message.reply_text('Bot started!')

def start_bot():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message_to_channel))

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
