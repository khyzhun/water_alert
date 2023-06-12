from telegram import Bot
from telegram.constants import ParseMode
import config_reader


async def send_alert(chat_id, found_keywords):
    if len(found_keywords) == 0:
        return
    message = "Знайдено ключові слова: {}".format(', '.join(found_keywords))
    bot = Bot(token=config_reader.BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


async def send_keywords_updated(chat_id):
    bot = Bot(token=config_reader.BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text="Ваші ключові слова успішно оновлено", parse_mode=ParseMode.HTML)


async def send_time_updated(chat_id):
    bot = Bot(token=config_reader.BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text="Час, коли буде перевірятись сайт успішно оновлено", parse_mode=ParseMode.HTML)
