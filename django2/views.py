# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return HttpResponse("Home Page.")
    # return redirect('account:login_form')
