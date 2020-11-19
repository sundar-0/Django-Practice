from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""One To One Relationship"""
class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()

"""One to Many Relationship"""
class UserPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=70)
    post_cat=models.CharField(max_length=70)
    post_publish_date=models.DateField()

"""Many To Many Relationship"""
class Song(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=70)
    song_duration=models.IntegerField()
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])
       
     