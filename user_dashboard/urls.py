from django.urls import path
from . import views

app_name = 'user_dashboard'

urlpatterns = [
    path('home/', views.user_home, name='user_dashboard_home'),  # الصفحة الرئيسية للمستخدمين
    path('readings-list/', views.readings_list, name='readings_list'),
    path('readings/add/', views.add_reading, name='add_reading'),  # تأكد أن هذا السطر موجود
    path('device/<int:device_id>/', views.device_details, name='device_details'),
    path('dashboard/', views.user_home, name='user_dashboard'),
    path('devices/', views.devices_list, name='devices_list'),  # المسار المطلوب
    path('readings/', views.readings_list, name='readings_list'),
    path('readings/', views.view_readings, name='view_readings'),

]
