from django.contrib import admin
from django.urls import path
from studentapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="addshow"),
    path('delete/<int:id>/',views.delete_student,name="deletestudent"),
    path('<int:id>',views.update_student,name="updatestudent"),
    path('signup/',views.sign_up,name="signup"),
    path('login/',views.Login,name="login"),
    path('profile/',views.Profile,name="profile"),
    path('logout/',views.Logout,name="logout"),
    path('changepass/',views.change_pass,name="changepass"),
    path('userdetail/<int:id>',views.userdetail,name="userdetail"),
    path('dashboard/',views.dashboard,name="dashboard")
]
