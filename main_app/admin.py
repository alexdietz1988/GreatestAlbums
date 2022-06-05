from django.contrib import admin
from .models import Album, Favorite, NotInterested, Listened, WantToListen

# Register your models here.
admin.site.register(Album)
admin.site.register(Favorite)
admin.site.register(NotInterested)
admin.site.register(Listened)
admin.site.register(WantToListen)