from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    author=models.CharField(max_length=100)
    created=models.DateTimeField(default=datetime.now())
