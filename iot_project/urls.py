from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shared_app.views import redirect_after_login



urlpatterns = [
    path('admin/', admin.site.urls),  # لوحة الإدارة
    path('', include('shared_app.urls')),  # الصفحة الرئيسية
    path('admin_dashboard/', include('admin_dashboard.urls', namespace='admin_dashboard')),
    path('user_dashboard/', include('user_dashboard.urls', namespace='user_dashboard')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect_after_login/', redirect_after_login, name='redirect_after_login'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
