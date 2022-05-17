import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.db.models import Q

import os
import http.client
import json

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
headers = {
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com",
    'X-RapidAPI-Key': "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
}
fixtures_leagues = {
    "all": "",
    "premier_league": 39,
    "ligue_1": 61,
    "serie_a": 135,
    "laliga": 140,
    "bundesliga": 78,
    "superliga": 286,
    "world_cup": 1,
    "uefa_champions_league": 2,
}


def livescores(request):
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
    data_refresh = "3600"

    context = {
        "data_host": data_host,
        "data_key": data_key,
        "data_refresh": data_refresh,
    }

    return render(request=request, template_name="livescores.html", context=context)


def fixtures(request: HttpRequest):
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
    data_refresh = "3600"
    data_date = str(datetime.datetime.today().date())
    data_league = fixtures_leagues["all"]
    data_season = ""

    if request.method == "POST":
        data_date = request.POST.get("datum")
        if data_date == "":
            data_date = str(datetime.datetime.today().date())
        data_league = fixtures_leagues[request.POST.get("lige")]

        chosen_year, chosen_month, chosen_day = data_date.split("-")
        between_seasons_date = datetime.date(int(chosen_year), 8, 15)
        chosen_date = datetime.date(int(chosen_year), int(chosen_month), int(chosen_day))
        data_season = int(chosen_year)
        if chosen_date < between_seasons_date:
            data_season -= 1

    context = {
        "data_host": data_host,
        "data_key": data_key,
        "data_refresh": data_refresh,
        "data_date": data_date,
        "data_league": data_league,
        "data_season": data_season,
    }

    return render(request=request, template_name="fixtures.html", context=context)


def manager(request: HttpRequest):
    players = None
    if request.method == "POST":
        search_name = request.POST.get("player")
        search_league = request.POST.get("player_league")

        conn.request("GET", "/v3/leagues?search=" + search_league, headers=headers)
        leagues = json.loads(conn.getresponse().read())["response"]

        players = []
        for i in range(min(len(leagues), 5)):
            conn.request("GET", "/v3/players?league=" + str(leagues[i]["league"]["id"]) +
                         "&search=" + search_name, headers=headers)
            players.extend(json.loads(conn.getresponse().read())["response"])
        players = players[:10]
    context = {
        "players": players,
    }
    return render(request=request, template_name="manager.html", context=context)


def manager_teams(request: HttpRequest, search):
    context = {
        "nesto": search,
    }
    return render(request=request, template_name="manager_players.html", context=context)


def manager_players(request: HttpRequest, search):
    context = {
        "nesto": search,
    }
    return render(request=request, template_name="manager_players.html", context=context)

