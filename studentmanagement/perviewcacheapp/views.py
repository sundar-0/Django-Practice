from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(30)
def home(request):
    return render(request,'perviewcacheapp/course.html')
def contact(request):
    return HttpResponse("<h1>Contact Field</h1>")
