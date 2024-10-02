from django.db import models


class Order(models.Model):
    """ Класс модели для работы ORM"""
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return f'{self.order_name} (id={self.id})'

    class Meta:
        # Имя модели для админки
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

