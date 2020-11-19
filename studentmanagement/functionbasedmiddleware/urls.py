from django.urls import path
from functionbasedmiddleware import views
urlpatterns = [
    path('',views.home,name="home")
]
