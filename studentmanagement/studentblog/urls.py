from django.urls import path
from studentblog import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.blog_dashboard,name="blog_dashboard"),
    path('logout/',views.user_logout,name="blog_logout"),
    path('login/',views.user_login,name="blog_login"),
    path('signup/',views.user_signup,name="blog_signup"),
    path('deleteblog/<int:id>',views.delete_blog,name="delete_blog"),
    path('editblog/<int:id>',views.edit_blog,name="edit_blog")
]