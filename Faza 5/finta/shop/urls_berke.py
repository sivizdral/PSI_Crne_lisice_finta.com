from django.contrib import admin
from django.urls import path
from .views_berke import *

urlpatterns = [
    path('livescores/', livescores, name='livescores'),
    path('fixtures/', fixtures, name='fixtures'),
]
