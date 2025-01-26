from django.urls import path
from . import views

app_name = 'shared_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('devices/', views.devices, name='devices'),
    path('reports/', views.reports, name='reports'),
    path('device/edit/<int:device_id>/', views.edit_device, name='edit_device'),
    # حذفنا path('readings/'...) من هنا
]