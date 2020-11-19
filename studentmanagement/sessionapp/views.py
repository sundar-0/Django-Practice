from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['fname']='sundar'
    request.session['lname']='dumre'
    return render(request,'sessionapp/setsession.html')

def getsession(request):
    if 'fname' and 'lname'  in request.session:
        fname=request.session['fname']
        lname=request.session['lname']
        request.session.modified=True
        return render(request,'sessionapp/getsession.html',{'fname':fname,'lname':lname})
    else:
        return HttpResponse('No Session Available!!!')

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'sessionapp/delsession.html')