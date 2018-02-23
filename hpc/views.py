from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, render_to_response
import logging

logger = logging.getLogger('mylogger')


# Create your views here.

def index(request):
    # logger.error('test logger')
    return render(request, 'hpc/index.html')
    # return HttpResponseServerError()
    # return HttpResponse(status=404)

def lalala(request):
    return HttpResponse(status=404)