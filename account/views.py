from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # is_valid() call the clean() method in LoginForm
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'],
                                     password=cd['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            return render(request, 'account/login.html', {'form': form})

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(reverse("account:login"))

