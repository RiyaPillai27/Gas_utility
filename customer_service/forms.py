# forms.py

from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer', 'request_type', 'details']

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']
