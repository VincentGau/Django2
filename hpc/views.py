from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    user_name = 'Noone'
    if request.user.is_authenticated:
        user_name = request.user
    return HttpResponse("Welcome, %s" % user_name)
