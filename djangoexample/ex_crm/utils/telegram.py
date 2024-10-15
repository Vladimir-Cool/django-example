import requests
from config.envs import settings_telegram

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    token = settings_telegram.TELEGRAM_BOT_TOKEN
    chat_id = settings_telegram.CHAT_ID


