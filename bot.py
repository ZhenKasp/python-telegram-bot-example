import logging
import os
import pdb
import datetime
import pytz

from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from dotenv import load_dotenv

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()

def start(update, context):
    print('BOT: Start')
    update.message.reply_text('Hi!')

def help(update, context):
    update.message.reply_text('Help!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def run_with_deley(update, context):
    job = updater.job_queue
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Message incoming")
    chat_id = update.effective_chat.id
    job.run_once(once, 10, context = chat_id)

def once(context: CallbackContext):
    message = "Hello, this message will be sent only once"
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text=message)

def schedule_message(update, context):
    job = updater.job_queue
    # breakpoint()
    chat_id = update.effective_chat.id

    daily_job = job.run_daily(send_common_information,
                              days = (0, 1, 2, 3, 4, 5, 6),
                              time = datetime.time(hour = 22, minute = 1, second = 00, tzinfo = pytz.timezone('Europe/Minsk')),
                              context = chat_id)
    print('daily job: ',daily_job.next_t)

def send_common_information(context: CallbackContext):
    message = 'common information'
    chat_id = context.job.context
    context.bot.send_message(chat_id = chat_id, text = message)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def updater():
    return Updater(os.getenv('TELEGRAM_BOT_TOKEN'), use_context = True)

def main():
    global updater
    updater = updater()

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("with_deley", run_with_deley))
    dp.add_handler(CommandHandler("schedule_message", schedule_message))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()