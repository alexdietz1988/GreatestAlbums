from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    image = models.CharField(max_length=500, default='')
    rank_2003 = models.IntegerField(default=0)
    rank_2012 = models.IntegerField(default=0)
    rank_2020 = models.IntegerField(default=0)
    year = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['rank_2020']

class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='userlists')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
    want_to_listen = models.BooleanField(default=False)
    not_interested = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    listened = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.album}'