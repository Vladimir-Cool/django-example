from django.db import models
from django.urls import reverse

class Order(models.Model):
    """ Класс модели для работы ORM"""
    class Meta:
        # Имя модели для админки
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        # Сартировка по умолчанию, для QuerySet '-id' - обратная сортировка
        ordering = ['id']

    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def get_absolute_url(self):
        """ Вернет ссылка на страницу с объектом"""
        return reverse('ex_crm:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.order_name} (id={self.id})'



