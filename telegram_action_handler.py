from telegram import Bot
from telegram.constants import ParseMode
import telegram_message_sender


def handle_set_keyword(keywords, contex):
    # TODO: save keywords as {chat_id:keywords}
    print(f'user keywords = {keywords}')
    telegram_message_sender.send_keywords_updated(contex.chat_id)


def handle_set_time(time, contex):
    # TODO: save keywords as {chat_id:keywords}
    print(f'user time = {time}')
    telegram_message_sender.send_keywords_updated(contex.chat_id)
