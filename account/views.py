from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.


def mylogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'],
                                     password=cd['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("success.")
            else:
                return HttpResponse('failed')
        else:
            return HttpResponse('invalid')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})