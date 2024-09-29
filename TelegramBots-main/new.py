from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging
import csv
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# File path for CSV
csv_file_path = 'user_messages52s.csv'

# Load existing data from CSV into a dictionary
def load_message_counts():
    message_counts = {}
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for rows in reader:
                try:
                    username, count = int(rows[0]), int(rows[1])
                    message_counts[username] = count
                except (ValueError, IndexError):
                    logger.error(f"Skipping invalid row: {rows}")
    return message_counts

# Save message counts to CSV
def save_message_counts(message_counts):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for username, count in message_counts.items():
            writer.writerow([username, count])

# In-memory message counts
message_counts = load_message_counts()

# Asynchronous function to handle messages
async def track_messages(update: Update, context):
    username = update.message.from_user.username
    message_counts[username] = message_counts.get(username, 0) + 1
    save_message_counts(message_counts)
    logger.info(f'Message counted for user {username}')
    await update.message.reply_text('Message counted!')


# Asynchronous function to report top users
async def report_top_users(update: Update, context):
    sorted_counts = sorted(message_counts.items(), key=lambda item: item[1], reverse=True)[:1000]
    report = "\n".join(f"User {username}: {count} messages" for username, count in sorted_counts)
    await update.message.reply_text(report if report else "No messages recorded yet.")

# Main function to create bot application
def main():
    application = Application.builder().token('7077731325:AAHIDWmJD29I51GUcyqhuRrc_mzgZq_Xh_o').build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_messages))
    application.add_handler(CommandHandler("topusers", report_top_users))
    application.run_polling()

if __name__ == '__main__':
    main()
