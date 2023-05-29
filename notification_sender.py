from telegram import Bot
from telegram.constants import ParseMode
import config_reader


async def send(chat_id, found_keywords):
    message = "Знайдено ключові слова: {}".format(', '.join(found_keywords))
    bot = Bot(token=config_reader.BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
