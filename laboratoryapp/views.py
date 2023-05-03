# Create your views here.
from django.shortcuts import render,redirect
from laboratoryapp.models import LaboratoryRegister,Test_category,Name_category,Appointment
from patientapp.models import UserRegister,Userfeedback
from laboratoryapp.forms import LaboratoryRegisterform,Testform



#lab signin page
def Lab_signin(request):
    if request.method=="POST":
        print(request.POST['Lid'])
        try:
            m = LaboratoryRegister.objects.get(Lid=request.POST['Lid'])
            if m.Laboratorypwd == request.POST['Laboratorypwd']:
                request.session['Lid'] = m.Lid
                request.session['name'] = m.Laboratoryfname
                request.session['fname'] = m.Laboratorymname
                request.session['mname'] = m.Laboratorylname

                return redirect('laboratory:index')
            else:
                return render(request,'Lab_signin.html',{'m':'Password incorrect'})
        except:
            return render(request,'Lab_signin.html',{'m':'Password incorrect'})
    return render(request,'Lab_signin.html')

def lab_home(request):
    if 'Lid' in request.session:
        a=LaboratoryRegister.objects.get(Lid=request.session['Lid'])
        b=Test_category.objects.all()
        return render(request,'index.html',{'a':a,'b':b,'c':len(b)})
    else:
        return redirect('laboratory:lab_signin')
    

        
# lab signup
def Lab_signup(request): 
    obj=LaboratoryRegisterform(request.POST,request.FILES)
    if obj.is_valid():
        data=LaboratoryRegister.objects.all().filter(Lid=request.POST['Lid'])
        print(len(data))
        if len(data)<=0: 
            obj.save()
            return redirect('laboratory:lab_signin')
        else:
            return render(request,'Lab_signup.html',{'messagekey':"User Already Exists"})
    return render(request,'Lab_signup.html')


#profile
def lab_profile(request):
    if 'Lid' in request.session:
        a=LaboratoryRegister.objects.get(Lid=request.session['Lid'])
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['passowrd']
            a.Laboratoryfname=name
            a.Lid=email
            a.Laboratorypwd=password
            a.save()
            return redirect('laboratory:index')
        return render(request,'lab_profile.html',{'n':a})
    else:
        return redirect('laboratory:lab_signin')
#lab logout
def logout(request):
    if 'Lid' in request.session:
        del request.session['Lid']
        return redirect('laboratory:lab_signin')
    else:
        return redirect('laboratory:lab_signin')


#view category
def view_category(request):
    if 'Lid' in request.session:
        b=Name_category.objects.all()
        return render(request,'view_category.html',{'b':b})
    else:
        return redirect('laboratory:lab_signin')


#add category
def add_category(request):
    a=Name_category.objects.all()
    if 'Lid' in request.session:
        if request.POST:
            name=request.POST['name']
            b=Name_category()
            b.category_name=name
            b.save()
            return redirect('laboratory:view_category')
        return render(request,'add_category.html',{'n':a})
    else:
        return redirect('laboratory:lab_signin')
#edit category
def edit_category(request,id):
    if 'Lid' in request.session:
        a=Name_category.objects.get(pk=id)
        if request.POST:
            name=request.POST['name']
            a.category_name=name
            a.save()
            return redirect('laboratory:view_category')
        return render(request,'edit_category.html',{'n':a})
    else:
        return redirect('laboratory:lab_signin')
def delete_category(request,id):
    if 'Lid' in request.session:
        obj=Name_category.objects.get(pk=id)
        obj.delete()
        return redirect('laboratory:view_category')
    return redirect('laboratory:lab_signin')

#show appointment
def show_appo(request):
    results=Appointment.objects.filter(status='pending')
    return render(request,'show_appointment.html',{'book':results})



#book appointment
def edit_appo(request,id):
    if 'Lid' in request.session.keys():
        a=LaboratoryRegister.objects.get(Lid=request.session['Lid'])
        book=Appointment.objects.get(pk=id)
        if request.POST:
            book.status=request.POST['boked']
            book.save()
            return redirect('laboratory:show_appointment')
        return render(request,'edit_appointment.html',{'book':book,'owner_data':a})
    else:
        return redirect('laboratory:lab_signin')

def view_approvedappo(request):
    if 'Lid' in request.session:
        b=Appointment.objects.filter(status='approved') & Appointment.objects.filter(appointment_booked=False)
       
        return render(request,'take_bloodtest.html',{'b':b})
    else:
        return redirect('laboratory:lab_signin') 
# take test
def take_test(request,id):
    if 'Lid' in request.session:
        a=request.session['fname']
        c=request.session['name']
        b=Appointment.objects.get(pk=id)
        form =Testform(request.POST)
        if form.is_valid():
            b.appointment_booked=request.POST['test']   
            form.save()
            b.save()
            
            return redirect('laboratory:index')
        return render(request,'bloodtest.html',{'a':a,'b':b,'c':c})
    else:
        return redirect('laboratory:lab_signin')
#view test
def view_test(request,id):
    if 'Lid' in request.session:
        b=Test_category.objects.get(pk=id)
        print(b.l_name)
        c=UserRegister.objects.get(uid=b.email)
        
        return render(request,'datatable1.html',{'b':b,'c':c})
    else:
        return redirect('laboratory:lab_signin')

def delete_test(request,id):
    if 'Lid' in request.session:
        obj=Test_category.objects.get(pk=id)
        obj.delete()
        return redirect('laboratory:index')
    return redirect('laboratory:lab_signin')

def view_feedback(request):
    if 'Lid' in request.session:
        obj=Userfeedback.objects.all()
        return render(request,'view_feedback.html',{'b':obj})
    return redirect('laboratory:lab_signin')

def show_feedback(request,id):
    if 'Lid' in request.session:
        obj=Userfeedback.objects.get(id=request.session['userId'])
        return render(request,'show_feedback.html',{'b':obj})
    return redirect('laboratory:lab_signin')