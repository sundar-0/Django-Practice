from django.shortcuts import render,HttpResponse
from customsignalapp import signals
# Create your views here.
def home(request):
    signals.notification.send(sender=None,request=request,user=["Sundar Dumre","Sujan Bhusal"])
    return HttpResponse('<h1>Custom Signal Demo.....</h1>')
