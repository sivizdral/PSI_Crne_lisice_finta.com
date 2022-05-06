from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('shop/', shop, name='shop'),
    path('login/', login_req, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_req, name='logout')
]