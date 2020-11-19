from django.urls import path
from relationshipApp import views
urlpatterns = [
    path('',views.home,name="home"),
    path('user/',views.user,name="user"),
    path('page/',views.page,name="page"),
    path('post/',views.post,name="post"),
    path('song/',views.song,name="song")
]
