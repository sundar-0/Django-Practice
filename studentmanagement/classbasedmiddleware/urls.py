from django.urls import path
from classbasedmiddleware import views
urlpatterns = [
    path('',views.home,name="home"),
    path('exc/',views.exception,name="exception")
]
