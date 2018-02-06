from django.urls import path


from django.contrib.auth import views
from . import views as myviews

app_name = 'account'
urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', myviews.mylogin, name='login'),
    path('logout/', views.logout, name='logout'),
]