from django.contrib import admin
from .models import Text, Tag


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'get_user', 'date_creation',
                    'date_last_change')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'get_code')
