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

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Клиент')
    content = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    def __str__(self):
        return f'{self.client_name}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
