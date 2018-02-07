from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def index(request):
    return render_to_response('hpc/index.html')


def page_not_found():
    return render_to_response('hpc/404.html')


def server_error():
    return render_to_response('hpc/404.html')