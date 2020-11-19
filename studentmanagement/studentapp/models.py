from django.db import models
# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_roll=models.IntegerField()
    stu_contact=models.IntegerField()
    stu_email=models.EmailField(max_length=100)
    stu_faculty=models.CharField(max_length=100)

class blog(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)







    
