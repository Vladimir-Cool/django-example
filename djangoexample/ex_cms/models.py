from django.db import models

class CmsSlider(models.Model):
    """ """
    class Meta:
        # Имя модели для админки
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        # Сартировка по умолчанию, для QuerySet '-id' - обратная сортировка
        ordering = ['id']

    # upload_to - указываем директорию внутри 'media'
    cms_url = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, verbose_name='CSS класс', null=True, default='-')

    def __str__(self):
        return self.cms_title

