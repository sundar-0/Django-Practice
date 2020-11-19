from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("I am Home View...")
    return HttpResponse("Home View")

def exception(request):
    print("I am Exception View")
    a=10/0
    return HttpResponse(a)

