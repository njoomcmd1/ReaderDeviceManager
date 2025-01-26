from django.contrib import admin
from .models import Reading, Device

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'temperature', 'manual_time', 'entry_time']
    list_filter = ['device', 'manual_time']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'device_number', 'function', 'location']
    search_fields = ['name', 'device_number']