from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Device, Reading
from .forms import DeviceForm
#مؤقت
from django.contrib.admin.views.decorators import staff_member_required
from user_dashboard.models import Reading
from admin_dashboard.models import Device  # استيراد نموذج الأجهزة
from .models import DeviceReading  # استيراد النموذج إذا كان موجودًا


# تعريف دالة للتحقق من صلاحيات المشرف
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الجهاز بنجاح')
            return redirect('admin_dashboard:dashboard')
    else:
        form = DeviceForm()
    return render(request, 'admin_dashboard/add_device.html', {'form': form})

@user_passes_test(is_admin)
def dashboard(request):
    devices = Device.objects.all()
    readings = Reading.objects.all().order_by('-entry_time')
    context = {
        'devices': devices,
        'readings': readings,
        'total_devices': devices.count(),
        'total_readings': readings.count()
    }
    return render(request, 'admin_dashboard/dashboard.html', {})

@user_passes_test(is_admin)
def manage_devices(request):
    devices = Device.objects.all()
    return render(request, 'admin_dashboard/manage_devices.html', {'devices': devices})


@user_passes_test(is_admin)
def edit_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث الجهاز بنجاح')
            return redirect('admin_dashboard:manage_devices')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'admin_dashboard/edit_device.html', {'form': form, 'device': device})

@user_passes_test(is_admin)
def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        device.delete()
        messages.success(request, 'تم حذف الجهاز بنجاح')
        return redirect('admin_dashboard:manage_devices')
    return render(request, 'admin_dashboard/delete_device.html', {'device': device})

@user_passes_test(is_admin)
def view_readings(request):
    readings = Reading.objects.all().order_by('-entry_time')
    return render(request, 'admin_dashboard/view_readings.html', {'readings': readings})


@staff_member_required
def dashboard(request):
    devices = Device.objects.all()  # جلب جميع الأجهزة
    readings = Reading.objects.all()  # جلب جميع القراءات
    return render(request, 'admin_dashboard/dashboard.html', {'devices': devices, 'readings': readings})

@staff_member_required
def dashboard(request):
    devices = Device.objects.all()  # جلب جميع الأجهزة
    return render(request, 'admin_dashboard/dashboard.html', {'devices': devices})

def admin_dashboard(request):
    # جلب جميع القراءات
    readings = Reading.objects.all()

    # جلب جميع الأجهزة
    devices = Device.objects.all()

    # تمرير البيانات إلى القالب
    return render(request, 'admin_dashboard/dashboard.html', {
        'readings': readings,
        'devices': devices,
    })


def admin_readings_view(request):
    readings = DeviceReading.objects.all()  # استعلام لجلب جميع البيانات
    return render(request, 'admin_dashboard/readings_list.html', {'readings': readings})