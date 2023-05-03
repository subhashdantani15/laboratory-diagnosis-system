from django.urls import path
from laboratoryapp.views import *

urlpatterns = [
    # signin,signup,indexpage
    path('',Lab_signin,name="lab_signin"),
    path('signup/',Lab_signup,name="lab_signup"),
    path('lab/',lab_home,name="index"),
    #profile
    path('lab_profile/',lab_profile,name="lab_profile"),
    #Logout
    path('logout/',logout,name='logout'),
    #add category
    path('add_category/',add_category,name='add_category'),
    #view category
    path('view_category/',view_category,name='view_category'),
    #edit category
    path('edit_category/<int:id>/',edit_category,name='edit_category'),
    path('delete_category/<int:id>/',delete_category,name='del_category'),
    #appointment show
    path('show_appointment/',show_appo,name='show_appointment'),
    # reject appointment
    # path('delete_test/<int:id>',delete_appointment,name='delete_appo'),
    #book appointment
    path('edit/<int:id>/',edit_appo,name="edit_appo"),
    # show approved appointment
    #book appointment
    path('show_test',view_approvedappo,name="view_approvedappo"),
    #take test
    path('take_test/<int:id>/',take_test,name='take_test'),
    #view test
    path('view_test/<int:id>/',view_test,name='view_test'),
    path('delete_test/<int:id>/',delete_test,name='delete_test'),
    path('read_feedback/',view_feedback,name='view_feedback'),
    path('read_feedback/<int:id>/',show_feedback,name='show_feedback'),

]