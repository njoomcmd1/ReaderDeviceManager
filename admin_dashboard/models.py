from django.db import models
from shared_app.models import Device  # استيراد نموذج الأجهزة من shared_app
from django.contrib.auth.models import User  # استيراد نموذج المستخدم

# نموذج لتسجيل إجراءات المشرف على الأجهزة
class AdminAction(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on {self.device.name}"


# نموذج لتسجيل معلومات الأجهزة
class Device(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الجهاز")
    device_number = models.CharField(max_length=255, verbose_name="رقم الجهاز")  # تأكد من وجود هذا الحقل
    function = models.CharField(max_length=255, verbose_name="وظيفة الجهاز")
    location = models.CharField(max_length=255, verbose_name="موقع الجهاز")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "جهاز"
        verbose_name_plural = "الأجهزة"


# نموذج لتسجيل قراءات الأجهزة (Reading)
class Reading(models.Model):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='general_readings',  # تغيير related_name لتجنب التعارض مع DeviceReading
        verbose_name="الجهاز"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='general_readings',  # تغيير related_name لتجنب التعارض مع DeviceReading
        verbose_name="المستخدم"
    )
    value = models.FloatField(verbose_name="القيمة")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإدخال")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    def __str__(self):
        return f"{self.device.name} - {self.value} - {self.entry_time}"

    class Meta:
        verbose_name = "قراءة"
        verbose_name_plural = "القراءات"
        ordering = ['-entry_time']


# نموذج آخر لتسجيل قراءات الأجهزة (DeviceReading)
class DeviceReading(models.Model):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='device_readings',  # تغيير related_name لتجنب التعارض مع Reading
        verbose_name="الجهاز"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='device_readings',  # تغيير related_name لتجنب التعارض مع Reading
        verbose_name="المستخدم"
    )
    value = models.FloatField(verbose_name="القيمة")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإدخال")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    def __str__(self):
        return f"{self.device.name} - {self.value} - {self.entry_time}"

    class Meta:
        verbose_name = "قراءة الجهاز"
        verbose_name_plural = "قراءات الأجهزة"
        ordering = ['-entry_time']
