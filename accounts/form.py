from django.forms import ModelForm
from django import forms

from accounts.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields= '__all__'
        exclude=['patient']