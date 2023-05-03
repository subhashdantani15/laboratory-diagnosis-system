from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from laboratoryapp.models import LaboratoryRegister,Name_category,Test_category,Appointment

class LaboratoryRegisterAdmin(admin.ModelAdmin):
    list_display=['Lid','Laboratoryfname','Laboratorymname','Laboratorylname','Laboratoryaddress','Laboratorycity','Laboratoryarea','Laboratorypincode','Laboratorycontactno','Laboratoryphoto']

admin.site.register(LaboratoryRegister,LaboratoryRegisterAdmin)
admin.site.register(Name_category)
admin.site.register(Test_category)
admin.site.register(Appointment)
admin.site.site_header = 'laboratory diagnosis system Administration'                    # default: "Django Administration"
admin.site.index_title = 'laboratory diagnosis system'                 # default: "Site administration"
admin.site.site_title = 'laboratory diagnosis system' 