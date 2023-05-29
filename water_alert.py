import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.constants import ParseMode
import asyncio
import config_reader


TELEGRAM_BOT_TOKEN = config_reader.get_bot_token()
TELEGRAM_CHAT_ID = config_reader.get_chat_id()
SITE_URL = config_reader.get_site_url()
KEYWORDS = ['призупиненя', 'минай', 'аварійні роботи', 'вихідних', 'травень', 'шановні', 'головна']


async def send_notification(chat_id, message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


async def check_water_supply():
    response = requests.get(SITE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    last_post = soup.find('h1', class_='entry-title')

    found_keywords = []
    for keyword in KEYWORDS:
        if keyword in last_post.text:
            found_keywords.append(keyword)

    if found_keywords:
        message = "Знайдено ключові слова: {}".format(', '.join(found_keywords))
        await send_notification(TELEGRAM_CHAT_ID, message)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_water_supply())
    loop.close()
