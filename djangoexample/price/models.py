from django.db import models

class PriceCard(models.Model):
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ['id']

    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')


    def __str__(self):
        return self.pc_value + ' руб.'


class PriceTable(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']

    pc_title = models.CharField(max_length=200, verbose_name='Услуга')
    pc_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pc_new_price = models.CharField(max_length=200, verbose_name='Новая цена')


    def __str__(self):
        return self.pc_title