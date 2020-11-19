from django.contrib import admin
from .models import Student,blog
# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=('id','stu_name','stu_roll','stu_contact','stu_email','stu_faculty')

@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    list_display=('id','title','desc')

