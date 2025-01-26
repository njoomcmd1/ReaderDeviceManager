from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Device, Reading
from django.contrib.auth.decorators import login_required, user_passes_test  # أضفنا user_passes_test هنا
from .forms import ReadingForm, DeviceForm
from admin_dashboard.models import Device  # استيراد نموذج الأجهزة
from user_dashboard.models import Reading
from shared_app.models import Device

# دالة للتحقق من صلاحيات المشرف
def is_admin(user):
    return user.is_authenticated and user.is_staff

# ======= Admin Dashboard Views =======
@user_passes_test(is_admin)
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'تم إضافة الجهاز بنجاح')
                return redirect('admin_dashboard:dashboard')
            except Exception as e:
                messages.error(request, 'حدث خطأ أثناء حفظ الجهاز')
    else:
        form = DeviceForm()
    return render(request, 'admin_dashboard/add_device.html', {'form': form})

@user_passes_test(is_admin)
def dashboard(request):
    try:
        devices = Device.objects.all()
        readings = Reading.objects.all().order_by('-entry_time')
        context = {
            'devices': devices,
            'readings': readings,
            'total_devices': devices.count(),
            'total_readings': readings.count()
        }
        return render(request, 'admin_dashboard/dashboard.html', context)
    except Exception as e:
        messages.error(request, 'حدث خطأ في تحميل لوحة التحكم')
        return redirect('home')

# ======= User Dashboard Views =======
from admin_dashboard.models import Device  # استيراد نموذج الأجهزة

@login_required
def add_reading(request):
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.save()
            messages.success(request, "تمت إضافة القراءة بنجاح!")
            return redirect('user_dashboard:readings_list')
    else:
        form = ReadingForm()

    # جلب جميع الأجهزة
    devices = Device.objects.all()  # تأكد أن هذا الجدول يحتوي على بيانات

    return render(request, 'user_dashboard/add_reading.html', {
        'form': form,
        'devices': devices  # تمرير الأجهزة إلى القالب
    })


@login_required
def dashboard_home(request):
    try:
        devices = Device.objects.all()
        readings = Reading.objects.all().order_by('-entry_time')[:5]
        context = {
            'devices': devices,
            'readings': readings,
        }
        return render(request, 'user_dashboard/user_home.html', context)
    except Exception as e:
        messages.error(request, 'حدث خطأ في تحميل الصفحة الرئيسية')
        return redirect('home')

@login_required
def readings_list(request):
    try:
        readings = Reading.objects.filter(user=request.user).order_by('-entry_time')
        return render(request, 'user_dashboard/readings_list.html', {
            'readings': readings
        })
    except Exception as e:
        messages.error(request, 'حدث خطأ في تحميل قائمة القراءات')
        return redirect('user_dashboard:dashboard_home')




# Optional: Add device details view for users
@login_required
def device_details(request, device_id):
    try:
        device = get_object_or_404(Device, id=device_id)
        device_readings = Reading.objects.filter(
            device=device,
            user=request.user
        ).order_by('-entry_time')
        
        context = {
            'device': device,
            'readings': device_readings,
            'total_readings': device_readings.count()
        }
        return render(request, 'user_dashboard/device_details.html', context)
    except Exception as e:
        messages.error(request, 'حدث خطأ في تحميل تفاصيل الجهاز')
        return redirect('user_dashboard:dashboard_home')


@login_required
def devices_list(request):
    devices = Device.objects.all()
    return render(request, 'user_dashboard/devices_list.html', {'devices': devices})   


@login_required
def user_home(request):
    readings = Reading.objects.filter(user=request.user)  # القراءات الخاصة بالمستخدم
    return render(request, 'user_dashboard/user_home.html', {'readings': readings})


def view_readings(request):
    readings = Reading.objects.all()  # جلب جميع القراءات من قاعدة البيانات
    return render(request, 'اسم_القالب.html', {'readings': readings})