# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='song_singer'
urlpatterns=[
    url(r'^(?P<index>.*)$',views.index,name='index'),
]