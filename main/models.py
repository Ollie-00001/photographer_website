from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название страницы')
    url = models.CharField(max_length=200, verbose_name='Адрес страницы')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['title']
