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

class MyList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Album)

    def __str__(self):
        return self.user.username