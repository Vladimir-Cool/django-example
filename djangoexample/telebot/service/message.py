import requests

from telebot.models import MessageSetting

def send_message(data: dict) -> None:
    """ Отправляет сообщение в чат с телеграм ботом"""
    message_obj: MessageSetting = MessageSetting.objects.get(id=1)
    api = 'https://api.telegram.org/bot'
    method = api + message_obj.bot.telegram_token + '/sendMessage'

    text = message_obj.message_text.format(name=data['order_name'], phone=data['order_phone'])

    req = requests.post(method,
                        data={
                            'chat_id': message_obj.chat.chat_id,
                            'text': text
                        })


