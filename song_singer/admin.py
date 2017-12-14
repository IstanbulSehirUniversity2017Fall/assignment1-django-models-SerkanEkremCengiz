from django.contrib import admin
from .models import SingerModel,SongModel
# Register your models here.

admin.site.register(SingerModel)
admin.site.register(SongModel)