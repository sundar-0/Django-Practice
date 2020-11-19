from django.urls import path
from sessionapp import views
urlpatterns = [
    path('setsession/',views.setsession,name="setsession"),
    path('getsession/',views.getsession,name="getsession"),
    path('delsession/',views.delsession,name="delsession")
]
