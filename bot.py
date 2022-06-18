import logging
import os
import pdb
import datetime
import pytz

from telegram import *
from telegram.ext import *
from dotenv import load_dotenv

from api.open_weather_map import OpenWeatherMap
from services.data_preparer_service import DataPreparerService

def help(update, context):
    update.message.reply_text('Help!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def schedule_message(update, context):
    job = updater.job_queue
    chat_id = update.effective_chat.id

    for x in range(5):
        daily_job = job.run_daily(send_common_information,
                                days = (0, 1, 2, 3, 4, 5, 6),
                                time = datetime.time(hour = 8 + (x * 3), minute = 00, second = 00, tzinfo = pytz.timezone('Europe/Minsk')),
                                context = chat_id)
        print('daily job: ', daily_job.next_t)

def message(update, context: CallbackContext):
    job = updater.job_queue
    chat_id = update.effective_chat.id

    job.run_once(send_common_information, 0, context = chat_id)

def send_common_information(context):
    data = OpenWeatherMap().get_weather_by_city_name('Batumi')
    weather_information = DataPreparerService().prepare_weather_data(data)

    chat_id = context.job.context
    context.bot.send_message(chat_id = chat_id, text = weather_information)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def updater():
    return Updater(os.getenv('TELEGRAM_BOT_TOKEN'), use_context = True)

def main():
    load_dotenv(override = True)

    global updater
    updater = updater()

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('schedule_message', schedule_message))
    dp.add_handler(CommandHandler('common_information', message))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main()