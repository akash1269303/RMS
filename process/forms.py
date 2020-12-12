from django import forms
from process.models import *

class RegistrationModel(forms.ModelForm):
    class Meta:
        exclude=('otp')