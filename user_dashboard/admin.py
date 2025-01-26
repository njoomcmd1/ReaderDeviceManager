from django.contrib import admin
from .models import Reading

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'user', 'temperature', 'entry_time']  # تم تغيير value إلى temperature
    list_filter = ['device', 'user', 'entry_time']
    search_fields = ['device__name', 'user__username']