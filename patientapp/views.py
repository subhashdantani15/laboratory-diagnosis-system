# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

from .models import UserRegister,Userfeedback
from .forms import UserRegisterForm
from laboratoryapp.forms import appointmentform
from laboratoryapp.models import Appointment,Name_category,Test_category,LaboratoryRegister
from django.contrib import messages
# User signin 
def signin(request):
    if request.POST:
        email = request.POST['uid']
        pass1 = request.POST['userpwd']
        try:
            valid = UserRegister.objects.get(uid=email,userpwd=pass1)
            if valid:
                request.session['user'] = email
                request.session['userId'] = valid.pk
                return redirect('user:index')
            else:
                return render(request,'signin1.html',{'m':'Password incorrect'})
        except:
            return render(request,'signin1.html',{'m':'Password incorrect'})
            #  return redirect('/signin/')
    return render(request,'signin1.html')

#User logout
def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('user:signin')
    return redirect('user:signin')

#User index
def index(request):
    if 'user' in request.session.keys():
        b=UserRegister.objects.get(id=request.session['userId'])
        x=Test_category.objects.filter(email=request.session['user'])
        return render(request,'index1.html',{'b':b,'x':x})
    return redirect('user:signin')

# User register
def signup(request):
    obj=UserRegisterForm(request.POST) 
    if obj.is_valid():
        data=UserRegister.objects.all().filter(uid=request.POST['uid'])
        if len(data)<=0:
            obj.save()
            return redirect('user:signin')
        else:
            return render(request,'signup.html',{'messagekey':"User Already Exists"})
    return render(request,'signup.html')
    

#Booking Appointment from user side
import datetime
from django.utils.dateparse import parse_datetime

def book_appointment(request):
    if 'user' in request.session.keys():
        a=Name_category.objects.all()
        b=UserRegister.objects.get(id=request.session['userId'])
        form = appointmentform(request.POST)
        #print(form)
        if form.is_valid():
            c=Appointment.objects.filter(email=request.POST['email'])  & Appointment.objects.filter(status='pending')
            if len(c)<=0:
                cDate = datetime.datetime.today()
                postDate = request.POST['schedule']
                postDateArray = postDate.split("T")
                cDateArray = str(cDate).split(" ")
                if parse_datetime(postDateArray[0]) >= parse_datetime(cDateArray[0]):    
                    form.save()
                    messages.success(request,'Your appoinement is booked.')
                else:
                    return render(request,'book_appointment.html',{'form':form,'ab':a,'b':b,'m':'select future date only'})
            else:
                return render(request,'book_appointment.html',{'form':form,'ab':a,'b':b,'m':'appointment alredy booked'})
        return render(request,'book_appointment.html',{'form':form,'ab':a,'b':b})
    return redirect('user:signin')

def view_test(request,id):
    if 'user' in request.session.keys():
        b=Test_category.objects.get(pk=id)
        c=UserRegister.objects.get(uid=b.email)
        
        return render(request,'datatable.html',{'b':b,'c':c})
    else:
        return redirect('user:signin')

def view_appo_status(request):
    if 'user' in request.session.keys():
        b=Appointment.objects.filter(email=request.session['user'])
        return render(request,'view_appointment.html',{'b':b})
    else:
        return redirect('user:signin')

def delete_appointment(request,id):
    if 'user' in request.session.keys():
        obj=Appointment.objects.get(pk=id)
        obj.delete()
        return redirect('user:view_approvedappo')
    return redirect('user:signin')

def user_feedback(request):
    if 'user' in request.session.keys():
        c=UserRegister.objects.get(id=request.session['userId'])
        print(c)
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            Feedback=request.POST['Feedback']
            a=Userfeedback()
            a.username=name
            a.useremail=email
            a.feedback=Feedback
            a.save()
            return redirect('user:index')
        return render(request,'user_feedback.html',{'n':c})
    else:
        return redirect('user:signin')

#profile
def user_profile(request):
    if 'user' in request.session.keys():
        a=UserRegister.objects.get(id=request.session['userId'])
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['passowrd']
            a.userfname=name
            a.uid=email
            a.userpwd=password
            a.save()
            return redirect('user:index')
        return render(request,'user_profile.html',{'n':a})
    else:
        return redirect('user:signin')

# Html To Pdf -------------------

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.http import HttpResponse

# Html To Pdf -------------------

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

# def GeneratePdf(request,id):
#     if 'user' in request.session.keys():
#         invo = Test_category.objects.get(id=id)
#         c=UserRegister.objects.get(uid=invo.email)
#         data = {'c':c,'b':invo}
#         pdf = render_to_pdf('datatable.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
#     else:
#         return redirect('user:signin')


