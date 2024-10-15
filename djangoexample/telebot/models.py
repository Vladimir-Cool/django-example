from django.db import models


class BotSetting(models.Model):
    """ Настройки для телеграмм бота"""
    name = models.CharField(max_length=200, unique=True)
    telegram_token = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'
        ordering = ['id']

    def __str__(self):
        return self.name


class MessageSetting(models.Model):
    """ Настройки для сообщения в телеграмм"""
    name = models.CharField(max_length=200, unique=True)
    message_text = models.TextField()
    bot = models.ForeignKey('BotSetting', on_delete=models.PROTECT, related_name='message')
    chat = models.ForeignKey('ChatSetting', on_delete=models.PROTECT, related_name='message')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['id']

    def __str__(self):
        return self.name


class ChatSetting(models.Model):
    """ Настройки для чатов в телеграмм"""
    name = models.CharField(max_length=200, unique=True)
    chat_id = models.CharField(max_length=200)

    # bot = models.ManyToManyField('BotSetting', related_name='chat',  null=True, blank=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['id']

    def __str__(self):
        return self.name


