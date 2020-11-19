from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
from .forms import SignUpForm,AddPostForm
from django.contrib import messages
from .models import Post

# Create your views here.
#student_blog Field

def index(request):
    post=Post.objects.all()
    return render(request,'studentblog/home.html',{'post':post})
def about(request):
    return render(request,'studentblog/about.html')

def contact(request):
    return render(request,'studentblog/contact.html')

def blog_dashboard(request):
    if request.user.is_authenticated: 
        if request.method=='POST':
            fm=AddPostForm(request.POST) 
            if fm.is_valid():
                title=fm.cleaned_data['title']
                desc=fm.cleaned_data['desc']
                addpost=Post(title=title,desc=desc,author=request.user.username)
                addpost.save()  
                messages.success(request,'Added Successfully')
                userpost=Post.objects.filter(author=request.user.username)
                return render(request,'studentblog/dashboard.html',{'user':request.user,'form':fm,'userpost':userpost})
        else:
            fm=AddPostForm()
            userpost=Post.objects.filter(author=request.user.username)
            print(userpost)
            return render(request,'studentblog/dashboard.html',{'user':request.user,'form':fm,'userpost':userpost})
    else:
        return HttpResponseRedirect('/blog/login/')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/blog/login/')
    else:
        return HttpResponse('You Need To Login')
        

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=SignUpForm(request.POST)
            if fm.is_valid():
                user=fm.save()
                group=Group.objects.get(name='Editor')
                user.groups.add(group)
        else:
            if not request.user.is_authenticated:
                fm=SignUpForm()
                messages.success(request,'Account Created Successfully!!!')
        return render(request,'studentblog/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/blog/dashboard')

def user_login(request):
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
                    return HttpResponseRedirect('/blog/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'studentblog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/blog/dashboard/')

def delete_blog(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            blog_id=Post.objects.get(pk=id)
            blog_id.delete()
            messages.add_message(request,messages.WARNING,'DELETED SUCCESSFULLY!!')
            return HttpResponseRedirect('/blog/dashboard/')
    else:
        return HttpResponseRedirect('/blog/login')
def edit_blog(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            uid=Post.objects.get(pk=id)
            fm=AddPostForm(request.POST,instance=uid)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.INFO,'UPDATED SUCCESSFULLY!!')
                return HttpResponseRedirect('/blog/dashboard')
        else:
            uid=Post.objects.get(pk=id)
            fm=AddPostForm(instance=uid)
            return render(request,'studentblog/update.html',{'form':fm})    
    else:
        return HttpResponseRedirect('/blog/login')


