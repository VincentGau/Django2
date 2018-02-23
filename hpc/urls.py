#coding=utf-8

from django.urls import path

from . import views

app_name = 'hpc'
urlpatterns = [
    path('', views.index, name='index'),
    path('lalala', views.lalala, name='lalala'),
]