from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Page, Testimonial

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_link')
    list_display_links = ('title',)
    search_fields = ('title', 'url')

    def url_link(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')
    url_link.short_description = 'Адрес страницы'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'content', 'created_at')
    search_fields = ('client_name', 'content')
    ordering = ('-created_at',)

    def __str__(self):
        return f'{self.client_name}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']