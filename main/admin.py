from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Page

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_link')
    list_display_links = ('title',)
    search_fields = ('title', 'url')

    def url_link(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')
    url_link.short_description = 'Адрес страницы'