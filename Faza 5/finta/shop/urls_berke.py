from django.contrib import admin
from django.urls import path
from .views_berke import *

urlpatterns = [
    path('livescores/', livescores, name='livescores'),
    path('fixtures/', fixtures, name='fixtures'),
    path('manager/', manager, name='manager'),
    path('manager_teams/<str:search>', manager_teams, name='manager_teams'),
    path('manager_players/<str:search>', manager_players, name='manager_players'),
    path('manager_player_display/<int:id_player>', manager_player_display, name='manager_player_display'),
    path('manager_team_display/<int:id_team>', manager_team_display, name='manager_team_display'),
]
