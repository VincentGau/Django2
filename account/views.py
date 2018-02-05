from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return HttpResponse("account main page.")


def login(request):

    if request.method == 'GET':
        return render(request, 'account/login_form.html')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Show an error page
            return redirect('/')
