from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Device, Reading
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


def home(request):
    # احصل على قائمة الأجهزة (اختياري)
    devices = Device.objects.all()[:6]  # جلب عدد محدود من الأجهزة للعرض
    return render(request, 'shared_app/home.html', {'devices': devices})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('shared_app:home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    
    return render(request, 'registration/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.')
                return redirect('shared_app:login')
            except:
                messages.error(request, 'اسم المستخدم موجود بالفعل.')
        else:
            messages.error(request, 'كلمتا المرور غير متطابقتين.')
    
    return render(request, 'registration/register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('shared_app:home')

@login_required
def devices(request):
    devices = Device.objects.all()
    return render(request, 'shared_app/devices.html', {
        'devices': devices
    })

@login_required
def reports(request):
    return render(request, 'shared_app/reports.html')

@login_required
def edit_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        # Add your device editing logic here
        pass
    return render(request, 'shared_app/edit_device.html', {
        'device': device
    })


# D:\مشروع نهائي\prrooject\shared_app\views.py
def redirect_after_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:  # إذا كان المستخدم مشرفًا
            return redirect(reverse('admin_dashboard:dashboard'))  # توجيه المشرف إلى لوحة التحكم
        else:  # إذا كان مستخدمًا عاديًا
            return redirect(reverse('user_dashboard:user_dashboard_home'))  # توجيه المستخدم إلى لوحة المستخدم
    return redirect(reverse('login'))  # إذا لم يكن مصادقًا
