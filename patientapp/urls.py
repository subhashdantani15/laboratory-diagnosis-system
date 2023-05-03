from django.urls import path
from  patientapp.views import *


urlpatterns = [

    #User Signin,Signup,Logout,IndexpagenIndexpage1
    path('',signin,name="signin"),
    path('index/',index,name="index"),
    path('signup/',signup,name="signup"),
    path('logout/',logout,name='logout'),
    path('book_appointment/',book_appointment,name="book_appointment"),
    path('view_test/<int:id>',view_test,name='view_test'),
    path('view_appointment_status/',view_appo_status,name="view_approvedappo"),
    path('delete_appo/<int:id>',delete_appointment,name='delete_appointment'),
    path('send_feedback/',user_feedback,name='user_feedback'),
    path('user_profile/',user_profile,name='user_profile'),
    # path('Generatedpdf/<int:id>',GeneratePdf,name="pdf"),


    
    
]