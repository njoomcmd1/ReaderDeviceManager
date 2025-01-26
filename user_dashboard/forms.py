from django import forms
from .models import Reading
from shared_app.models import Device

class ReadingForm(forms.ModelForm):
    """
    نموذج لإضافة قراءة جديدة.
    """
    class Meta:
        model = Reading
        fields = ['device', 'temperature', 'manual_time']
        widgets = {
            'manual_time': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'placeholder': 'اختر وقت القياس'
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'temperature': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'أدخل درجة الحرارة'
                }
            ),
            'device': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'device': 'الجهاز',
            'temperature': 'درجة الحرارة',
            'manual_time': 'وقت القياس اليدوي',
        }
        error_messages = {
            'device': {
                'required': 'يرجى اختيار الجهاز.',
            },
            'temperature': {
                'required': 'يرجى إدخال درجة الحرارة.',
                'invalid': 'درجة الحرارة المدخلة غير صالحة.',
            },
            'manual_time': {
                'required': 'يرجى إدخال وقت القياس.',
                'invalid': 'وقت القياس المدخل غير صالح.',
            },
        }

    def clean_temperature(self):
        """
        التحقق من صحة درجة الحرارة.
        """
        temperature = self.cleaned_data.get('temperature')
        if temperature < -50 or temperature > 100:
            raise forms.ValidationError("درجة الحرارة يجب أن تكون بين -50 و 100.")
        return temperature


class DeviceForm(forms.ModelForm):
    """
    نموذج لإضافة أو تعديل جهاز.
    """
    class Meta:
        model = Device
        fields = ['name', 'device_number', 'function', 'location']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'اسم الجهاز'
                }
            ),
            'device_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'رقم الجهاز'
                }
            ),
            'function': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'وظيفة الجهاز'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'موقع الجهاز'
                }
            ),
        }
        labels = {
            'name': 'اسم الجهاز',
            'device_number': 'رقم الجهاز',
            'function': 'وظيفة الجهاز',
            'location': 'الموقع',
        }
        error_messages = {
            'name': {'required': 'يرجى إدخال اسم الجهاز.'},
            'device_number': {'required': 'يرجى إدخال رقم الجهاز.'},
        }
