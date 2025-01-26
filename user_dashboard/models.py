from django.db import models
from django.contrib.auth.models import User
from shared_app.models import Device
from django.utils import timezone
from admin_dashboard.models import Device  # تأكد أن جهاز مرتبط بالتطبيق المناسب

from django.db import models
from django.contrib.auth.models import User
from shared_app.models import Device
from django.utils import timezone
from admin_dashboard.models import Device  # تأكد أن جهاز مرتبط بالتطبيق المناسب

class Reading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='dashboard_readings', verbose_name="الجهاز")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_user_readings', verbose_name="المستخدم")
    temperature = models.FloatField(default=0.0, verbose_name="درجة الحرارة")
    manual_time = models.DateTimeField(default=timezone.now, verbose_name="الوقت اليدوي")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإدخال التلقائي")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    def __str__(self):
        return f"{self.device.name} - درجة الحرارة: {self.temperature}"

    class Meta:
        verbose_name = "قراءة"
        verbose_name_plural = "القراءات"
        ordering = ['-entry_time']