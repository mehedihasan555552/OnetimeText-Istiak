from django.contrib import admin
from .models import OneTimeText


@admin.register(OneTimeText)
class OneTimeTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_content', 'created_at')
    search_fields = ('content',)
    ordering = ('id',)
    list_per_page = 20

    def short_content(self, obj):
        return obj.content[:90]
    short_content.short_description = 'Content'
