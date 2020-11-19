from django.urls import path
from persitecacheapp import views
urlpatterns = [
    path('home/',views.home,name="home")
]