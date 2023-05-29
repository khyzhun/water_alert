import configparser

config = configparser.RawConfigParser()
config.read('telegram_bot.properties')

BOT_TOKEN = config.get('TELEGRAM', 'BOT_TOKEN')
BOT_ID = config.get('TELEGRAM', 'BOT_ID')
CHAT_ID = config.get('TELEGRAM', 'CHAT_ID')  # todo: might be dynamic and as a list of chats.
SITE_URL = config.get('SITE', 'URL')