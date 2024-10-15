import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv(dotenv_path="config/.env")


class SettingDjango(BaseSettings):
    """Класс настроек для Django"""
    SECRET_KEY: str = os.getenv('SECRET_KEY')


class SettingsTelegram(BaseSettings):
    """Класс настроек для телеграм бота"""
    TELEGRAM_BOT_TOKEN_1: str = os.getenv('TELEGRAM_BOT_TOKEN_1')
    CHAT_ID: str = os.getenv('CHAT_ID')


settings_django = SettingDjango()
settings_telegram = SettingsTelegram()

