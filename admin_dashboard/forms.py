from django import forms
from shared_app.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_number', 'function', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'device_number': forms.TextInput(attrs={'class': 'form-control'}),
            'function': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }