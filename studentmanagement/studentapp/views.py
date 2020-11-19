from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student
from django.contrib import messages
from .forms import SignUpForm,EditUserForm,EditAdminForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['stu_name']
            roll=fm.cleaned_data['stu_roll']
            contact=fm.cleaned_data['stu_contact']
            email=fm.cleaned_data['stu_email']
            faculty=fm.cleaned_data['stu_faculty']
            reg=Student(stu_name=name,stu_roll=roll,stu_contact=contact,stu_email=email,stu_faculty=faculty)
            reg.save()
            messages.add_message(request,messages.SUCCESS,'ADDED SUCCESSFULLY!!')
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=Student.objects.all()
    return render(request,'studentapp/addshow.html',{'form':fm,'student':stud})

def delete_student(request,id):
    if request.method=='POST':
        uid=Student.objects.get(pk=id)
        uid.delete()
        messages.add_message(request,messages.WARNING,'DELETED SUCCESSFULLY!!')
        return HttpResponseRedirect('/')
def update_student(request,id):
    if request.method=='POST':
        uid=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=uid)
        if fm.is_valid:
            fm.save()
            messages.add_message(request,messages.INFO,'UPDATED SUCCESSFULLY!!')
    else:
        uid=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=uid)
    return render(request,'studentapp/update.html',{'id':id,'form':fm})

#user Sign_up(UserCreationForm class)
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
        fm=SignUpForm()
        messages.success(request,'Account Created Successfully!!!')
    return render(request,'studentapp/signup.html',{'form':fm})

#login form
def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'studentapp/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
   

#profile
def Profile(request):
    if request.user.is_authenticated:  
        if request.method=='POST':
            if request.user.is_superuser==True:
                fm=EditAdminForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserForm(request.POST,instance=request.user)
                users= None
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile Updated Successfully!!')
                return render(request,'studentapp/profile.html',{'name':request.user,'form':fm,'users':users})
        else:
            if request.user.is_superuser==True:
                fm=EditAdminForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserForm(instance=request.user)
                users= None
            return render(request,'studentapp/profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')
    


#logout
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password Changed Successfully!!')
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'studentapp/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def userdetail(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminForm(instance=pi)
        return render(request,'studentapp/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


def dashboard(request):
    if request.user.is_authenticated:  
        return render(request,'studentapp/dashboard.html',{'username':request.user.username})
    else:
        return HttpResponseRedirect('/login/')




