from django.db import models
from patientapp.models import *
# Create your models here.
from django.db import models


# Doctor Details
class LaboratoryRegister(models.Model):
    Lid=models.EmailField(max_length=50,verbose_name='Email')
    Laboratorypwd=models.CharField(max_length=20,verbose_name='Password')
    Laboratoryfname=models.CharField(max_length=20,default='',verbose_name='Laboratory_Name')
    Laboratorymname=models.CharField(max_length=20,default='',verbose_name='First_Name')
    Laboratorylname=models.CharField(max_length=20,default='',verbose_name='Last_Name')
    Laboratoryaddress=models.CharField(max_length=20,default='',verbose_name='Address')
    Laboratorycity=models.CharField(max_length=20,default='',verbose_name='City')
    Laboratoryarea=models.CharField(max_length=20,default='',verbose_name='Area')
    Laboratorypincode=models.IntegerField(default='',verbose_name='Pincode')
    Laboratorycontactno=models.IntegerField(default='',verbose_name='Contact_No')
    Laboratoryphoto = models.FileField(upload_to   = 'upload',verbose_name='Laboratory certificate')
    
    def __str__(self):
        return self.Lid

class Name_category(models.Model):
    category_name=models.CharField(max_length=200,default='',verbose_name='Blood Test Name')
    
    def __str__(self):
        return self.category_name


class Test_category(models.Model):
    l_name=models.CharField(max_length=200,default='',verbose_name='Lab Assistance Name')
    lab_name=models.CharField(max_length=200,default='',verbose_name='Lab Name')
    Test_name=models.CharField(max_length=200,default='',verbose_name='Blood Test Name')
    patientname=models.CharField(max_length=200,default='',verbose_name='Patient Name')
    email = models.EmailField(default="")
    Haemoglobin=models.PositiveIntegerField(default="")
    RBC_Count=models.PositiveIntegerField(default="")
    PCV=models.PositiveIntegerField(default="")
    MCV=models.PositiveIntegerField(default="")
    MCH=models.PositiveIntegerField(default="")
    MCHC=models.PositiveIntegerField(default="")
    RDW=models.PositiveIntegerField(default="")
    Total_WBC_Count=models.PositiveIntegerField(default="")
    Neutrophils=models.PositiveIntegerField(default="")
    Lymphocytes=models.PositiveIntegerField(default="")
    Eosinophils=models.PositiveIntegerField(default="")
    Monocytes=models.PositiveIntegerField(default="")
    Basophils=models.PositiveIntegerField(default="")
    Platelet_Count =models.PositiveIntegerField(default="")
    WBCs_on_PS=models.CharField(max_length=50,default="")
    date_of_test=models.DateField(auto_created=True,auto_now=True)
    
    def __str__(self):
        return str(self.Test_name)

class Reference_Test_category(models.Model):
    Haemoglobin_reference = models.TextField(default="male : 14 - 16g \n Female : 12 - 14 g")
    RBC_reference = models.TextField(default="14 - 16g%")
    PCV_reference = models.TextField(default="35 - 45 %")
    MCV_reference = models.TextField(default="80 - 99 fl")
    MCH_reference = models.TextField(default="28 - 32 pg")
    MCHC_reference = models.TextField(default="30 - 34 %")
    RDW_reference = models.TextField(default="9 - 17 fl")
    Total_WBC_Count_reference = models.TextField(default="4000 - 11000 / cu.mm")
    Neutrophils_reference = models.TextField(default="40 - 75 %")
    Lymphocytes_reference = models.TextField(default="20 - 45 %")
    Eosinophils_reference = models.TextField(default="00 - 06 %")
    Monocytes_reference = models.TextField(default="00 - 10 %")
    Basophils_reference = models.TextField(default="00 - 01 %")
    Platelet_Count_reference = models.TextField(default="150000 - 450000 / cu.mm")
        
    def __str__(self):
        return str(self.Test_name)


class Appointment(models.Model):
    g = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    name = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    schedule = models.DateTimeField()
    Test_name=models.ForeignKey(Name_category, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=g, default = 'pending')
    appointment_booked=models.BooleanField(default=False)
    def __str__(self):
        return self.name