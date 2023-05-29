import requests
from bs4 import BeautifulSoup
import asyncio
import config_reader
import notification_sender

KEYWORDS = ['призупиненя', 'минай', 'аварійні роботи', 'вихідних', 'травень', 'шановні', 'головна']


async def check_water_supply():
    response = requests.get(config_reader.SITE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'### soup={soup}')
    last_post = soup.find('h1', class_='entry-title')
    print(f'### last_post={last_post}')

    found_keywords = []
    for keyword in KEYWORDS:
        if keyword in last_post.text:
            found_keywords.append(keyword)

    if found_keywords:
        await notification_sender.send(config_reader.CHAT_ID, found_keywords)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_water_supply())
    loop.close()
