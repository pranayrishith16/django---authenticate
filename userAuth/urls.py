from operator import index
from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.login, name='login'),
    path('home/',views.home, name='home')
]
