import configparser

config = configparser.RawConfigParser()
config.read('telegram_bot.properties')


def get_bot_token():
    return config.get('TELEGRAM', 'BOT_TOKEN')


def get_bot_id():
    return config.get('TELEGRAM', 'BOT_ID')


def get_chat_id():
    return config.get('TELEGRAM', 'CHAT_ID')


def get_site_url():
    return config.get('SITE', 'URL')