from django.db import models

# Create your models here.

class SingerModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_day=models.DateField()
    number_of_songs=models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+self.first_name+' '+self.last_name


class SongModel(models.Model):
    name=models.CharField(max_length=50)
    singer=models.ForeignKey(SingerModel,on_delete=models.CASCADE)
    lyrics=models.CharField(max_length=500)
    publish_day=models.DateField()
    producer=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)+' '+self.name


