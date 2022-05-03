from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('shop/', shop, name='shop'),
]