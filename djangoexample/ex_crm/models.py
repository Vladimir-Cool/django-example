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
    order_status = models.ForeignKey('StatusCrm', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def get_absolute_url(self):
        """ Вернет ссылка на страницу с объектом"""
        return reverse('ex_crm:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.order_name} (id={self.id})'


class StatusCrm(models.Model):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']

    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name


class CommentCrm(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_binding = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


    def __str__(self):
        return self.comment_text


