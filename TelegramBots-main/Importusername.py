from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Send me a user ID and I will tell you the username.')

async def get_username(update: Update, context: CallbackContext) -> None:
    user_id = update.message.text
    try:
        user = await context.bot.get_chat(user_id)
        if user.username:
            await update.message.reply_text(f'The username is @{user.username}')
        else:
            await update.message.reply_text("This user has no username or cannot be found.")
    except Exception as e:
        await update.message.reply_text(str(e))

def main() -> None:
    application = Application.builder().token('6774462761:AAHPkL1xQZWuqruldZy9FkyfCqxtZwstPR4').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_username))

    application.run_polling()

if __name__ == '__main__':
    main()
