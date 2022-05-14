from django.contrib import admin
from django.urls import path

from shop.views_kolja import team, teamsearch, player

urlpatterns = [
    path('team/', team, name='team'),
    path('teamsearch/', teamsearch, name='teamsearch'),
    path('player/', player, name='player'),
]