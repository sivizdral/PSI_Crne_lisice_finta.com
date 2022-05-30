from django.contrib import admin
from django.urls import path
from .views_slavko import *

urlpatterns = [
    path('myprofile/', myprofile, name='myprofile'),
    path('champs/', finta_champs, name='champs'),
    path('champs_register/', champs_register, name='champs_register'),
    path('champs_view/<int:id>', seeChampionship, name='champs_view'),
    path('ranklist/', ranklist, name='ranklist')
]