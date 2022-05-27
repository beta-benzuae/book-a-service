from django.forms import ModelForm, Textarea, TextInput, FileInput,URLInput,Select,BooleanField,DateInput
from django.utils.translation import ugettext_lazy as _
from django import forms
from web.models import *


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['creator', 'updater', 'auto_id', 'is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': ' ', 'placeholder': 'Your Name'}),
            'email': TextInput(attrs={'class': 'email  ', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': ' ', 'placeholder': 'Contact Number'}),
            'vehicle_number': TextInput(attrs={'class': '   ', 'placeholder': 'Vehicle Number'}),
            'kms_driven': TextInput(attrs={'class': ' ', 'placeholder': 'Kilometers Driven'}),
            'time' : Select(attrs={'class':'',}),
            'date': DateInput(format=('%d-%m-%Y'), attrs={'type':'date', 'class':'','placeholder':'Select date'}),
            'message': TextInput(attrs={'class': ' w-100 ', 'placeholder': 'Service Needed'}),
        }

    error_messages = {
        
    }