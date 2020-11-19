from django.shortcuts import render
from .models import Page,UserPost,Song,User
# Create your views here.
def home(request):
    return render(request,'relationshipApp/home.html')
def user(request):
    data1=User.objects.all()
    data2=User.objects.filter(email='bibek@gmail.com')
    data3=User.objects.filter(page__page_cat='Programming')
    data4=User.objects.filter(userpost__post_publish_date='2020-11-01')
    data5=User.objects.filter(song__song_duration=3)
    return render(request,'relationshipApp/user.html',{'data1':data1,'data2':data2,
    'data3':data3,'data4':data4,'data5':data5})
def page(request):
    return render(request,'relationshipApp/page.html')
def post(request):
    return render(request,'relationshipApp/post.html')
def song(request):
   return render(request,'relationshipApp/song.html')

