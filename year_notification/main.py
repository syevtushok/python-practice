import calendar
import json
from datetime import datetime

import telebot


def lambda_handler(event, context):
    bot = telebot.TeleBot('BOT_TOKEN')

    today = datetime.now()
    day_of_year = today.timetuple().tm_yday

    total_days_in_year = 366 if calendar.isleap(today.year) else 365

    passed = "{0:.2%} days of the year have already passed.".format(day_of_year / total_days_in_year)
    bot.send_message("userId", passed)

    return {

        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
