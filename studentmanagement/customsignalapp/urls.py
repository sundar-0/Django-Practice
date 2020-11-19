from django.urls import path
from customsignalapp import views
urlpatterns = [
  path('',views.home,name="home")
]
