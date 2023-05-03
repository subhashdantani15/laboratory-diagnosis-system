from django import forms
from laboratoryapp.models import LaboratoryRegister,Appointment,Test_category


class LaboratoryRegisterform(forms.ModelForm):
    class Meta:
        model=LaboratoryRegister
        fields='__all__'



class appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields= '__all__'


class Testform(forms.ModelForm):
    class Meta:
        model = Test_category
        fields= '__all__'