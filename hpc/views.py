from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def index(request):
    return render(request, 'hpc/index.html')


def page_not_found():
    return render('hpc/404.html')


def server_error():
    return render('hpc/404.html')