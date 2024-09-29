import logging
import csv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Bot token obtained from BotFather
TOKEN = ''

# Function to start the bot and send a welcome message
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am here to collect User IDs and Usernames.')

# Function to handle all messages and collect user data
def collect_user_data(update: Update, context: CallbackContext):
    """Collect user data from each message."""
    if update.message and update.message.text:  # Check if there is text in the message directly
        user = update.message.from_user
        user_id = user.id  # User ID
        username = user.username if user.username else "No Username"  # Username or placeholder

        try:
            with open('user_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, username])
            logging.info(f"Saved user data: {user_id}, {username}")
        except Exception as e:
            logging.error(f"Error writing to CSV: {e}")
    else:
        logging.warning("Received update with no message or user information.")

# Main function to start the bot
def main():
    # Initialize the updater with your bot's token
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    application = Application.builder().token('6774462761:AAHPkL1xQZWuqruldZy9FkyfCqxtZwstPR4').build()

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(None, collect_user_data))  # We remove Filters.text and handle checking within the function

    # Start the Bot using polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
