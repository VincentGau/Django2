from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    # path('login_form/', views.login_form, name='login_form'),
    path('login/', views.login, name='login'),
]