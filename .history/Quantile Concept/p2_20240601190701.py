import logging
from telethon import TelegramClient, events
from telegram import Bot
from queue import Queue
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

# Initialize the Telegram client with bot token
client = TelegramClient('session_name', API_ID, API_HASH)

# Initialize the bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def forward_message_to_channel(event):
    message = event.message.message
    # Define your filter condition here
    if 'Message by : SAURABH SAHU' in message:  # Replace 'your keyword' with the actual keyword
        await bot.send_message(chat_id=DESTINATION_CHANNEL_ID, text=message)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    await forward_message_to_channel(event)

def start_bot():
    def start(update, context):
        update.message.reply_text('Bot started!')

    bot.message_handlers.append((start, "/start"))
    
    bot.start_polling()
    bot.idle()

if __name__ == '__main__':
    # Start the Telegram client
    client.start()

    # Start the bot in a new thread
    threading.Thread(target=start_bot).start()

    # Run the client
    client.run_until_disconnected()
