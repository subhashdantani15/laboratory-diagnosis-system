from django import forms
from patientapp.models import UserRegister

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields='__all__'
