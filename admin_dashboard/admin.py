from django.contrib import admin
from .models import AdminAction
from .models import Device, Reading


@admin.register(AdminAction)
class AdminActionAdmin(admin.ModelAdmin):
    list_display = ('device', 'action', 'timestamp')
    list_filter = ('device', 'timestamp')
    search_fields = ('device__name', 'action')
    ordering = ('-timestamp',)
    date_hierarchy = 'timestamp'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'user', 'value', 'entry_time']
    list_filter = ['device', 'user', 'entry_time']
    search_fields = ['device__name', 'user__username'] 