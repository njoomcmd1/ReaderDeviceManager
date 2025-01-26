from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الجهاز")
    device_number = models.CharField(max_length=50, verbose_name="رقم الجهاز")
    function = models.TextField(verbose_name="وظيفة الجهاز")
    location = models.CharField(max_length=200, verbose_name="الموقع")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "جهاز"
        verbose_name_plural = "الأجهزة"

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='shared_readings', verbose_name="الجهاز")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_user_readings', verbose_name="المستخدم")
    temperature = models.FloatField(default=0.0, verbose_name="درجة الحرارة")
    manual_time = models.DateTimeField(default=timezone.now, verbose_name="الوقت اليدوي")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإدخال التلقائي")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    class Meta:
        verbose_name = "قراءة"
        verbose_name_plural = "القراءات"
        ordering = ['-entry_time']