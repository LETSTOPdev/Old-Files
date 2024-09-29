from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Bot is now active.')

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"Echo: {text}")

def main():
    TOKEN = '6774462761:AAHPkL1xQZWuqruldZy9FkyfCqxtZwstPR4'  # Replace with your actual bot token
    updater = Updater(TOKEN)

    # Command handler for start command
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Message handler for all other messages
    updater.dispatcher.add_handler(MessageHandler(None, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
