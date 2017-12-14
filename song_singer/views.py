from django.shortcuts import render
from .models import SongModel,SingerModel

# Create your views here.

def index(request,index):
    detail=SongModel.objects.get(pk=index)
    return render(request,'detail.html',{'detail':detail})