from django.contrib import admin

from .models import Subscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    list_per_page = 10
    list_filter = ['created_at',]