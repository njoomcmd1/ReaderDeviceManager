from django.urls import path
from . import views
from .views import admin_readings_view

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('devices/', views.manage_devices, name='manage_devices'),
    path('devices/add/', views.add_device, name='add_device'),
    path('devices/edit/<int:device_id>/', views.edit_device, name='edit_device'),
    path('devices/delete/<int:device_id>/', views.delete_device, name='delete_device'),
    path('readings/', views.view_readings, name='view_readings'),
    path('readings/', admin_readings_view, name='readings_list'),

]