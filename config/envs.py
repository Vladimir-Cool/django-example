import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv(dotenv_path="config/.env")


class SettingDjango(BaseSettings):
    """Класс настроек для Django"""
    SECRET_KEY: str = os.getenv('SECRET_KEY')


settings_django = SettingDjango()
