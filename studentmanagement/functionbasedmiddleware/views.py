from django.shortcuts import render

# Create your views here.
def home(request):
    print("View is Called....")
    return render(request,'functionbasedmiddleware/home.html')
