import requests
from bs4 import BeautifulSoup
import asyncio
import config_reader
import telegram_message_sender
from datetime import datetime, date

KEYWORDS = ['призупинення', 'минай', 'аварійними']


def get_posts():
    response = requests.get(config_reader.SITE_URL)
    if not response.status_code == 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    post_elements = soup.find_all('article')
    print(f'soup={soup}')
    posts = []
    for post_element in post_elements:
        post_title = post_element.find('h1', class_='entry-title').text
        post_date = post_element.find('time', class_='entry-date published').text
        posts.append({'title': post_title, 'date': post_date})
    return posts


def filter_posts(posts):
    today = date.today()
    result = []
    for post in posts:
        post_date = datetime.strptime(post['date'], config_reader.SITE_DATE_FORMAT).date()
        if post_date >= today:
            result.append(post)
    return result


def search_keywords(posts, keywords):
    found_keywords = []
    for post in posts:
        for keyword in keywords:
            if keyword in post['title']:
                found_keywords.append(keyword)
                break  # If we come across at least one keyword, we can proceed to the next post.
    return found_keywords


async def check_water_supply():
    all_posts = get_posts()
    filtered_posts = filter_posts(all_posts)
    found_keywords = search_keywords(filtered_posts, KEYWORDS)
    await telegram_message_sender.send_alert(config_reader.CHAT_ID, found_keywords)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_water_supply())
    loop.close()
