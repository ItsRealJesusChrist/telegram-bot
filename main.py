import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update : Update,context : CallbackContext):
    update.message.reply_text("Hello world!")


def main():
    updater = Updater("1429895923:AAEOHo65zz0pjjBNBJo0Wi_z8fT6qs9Am-I",use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start",start))
    #dispatcher.add_handler(MessageHandler("ربات",start))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
