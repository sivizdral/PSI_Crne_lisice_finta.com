from django.contrib import admin
from django.urls import path
from .views_slavko import *

urlpatterns = [
    path('myprofile/', myprofile, name='myprofile'),
]