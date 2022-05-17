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


def calculate_current_season():
    current_date = datetime.datetime.today().date()
    between_seasons_date = datetime.date(current_date.year, 8, 1)
    current_season = current_date.year
    if current_date < between_seasons_date:
        current_season -= 1
    return current_season


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
        between_seasons_date = datetime.date(int(chosen_year), 8, 1)
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


# VECI DEO KODA JE POZAJMLJEN OD KOLJE
# def player in views_kolja.py
def manager_player_display(request: HttpRequest, id_player):
    current_season = calculate_current_season()

    conn.request("GET", "/v3/players?id=" + str(id_player) + "&season=" + str(current_season), headers=headers)
    data = json.loads(conn.getresponse().read())
    statistics = []
    for temp in data["response"][0]["statistics"]:
        if (temp["league"]["name"] != "Club Friendlies") and (temp["league"]["name"] != "Friendlies"):
            statistics.append({
                "leagueId": temp["league"]["id"],
                "leagueName": temp["league"]["name"],
                "leagueLogo": temp["league"]["logo"],
                "leagueCountry": temp["league"]["country"],
                "appearences": temp["games"]["appearences"],
                "lineups": temp["games"]["lineups"],
                "in": temp["substitutes"]["in"],
                "minutes": temp["games"]["minutes"],
                "rating": temp["games"]["rating"],
                "totalshots": temp["shots"]["total"],
                "onshots": temp["shots"]["on"],
                "goals": temp["goals"]["total"],
                "assists": temp["goals"]["assists"],
                "saves": temp["goals"]["saves"],
                "passes": temp["passes"]["total"],
                "keypasses": temp["passes"]["key"],
                "tackles": temp["tackles"]["total"],
                "totalduels": temp["duels"]["total"],
                "winduels": temp["duels"]["won"],
                "dribbles": temp["dribbles"]["success"],
                "yellowcards": temp["cards"]["yellow"],
                "redcards": temp["cards"]["red"],
                "scoredpenalty": temp["penalty"]["scored"],
                "missedpenalty": temp["penalty"]["missed"],
            })

    info = {
        'name': data["response"][0]["player"]["name"],
        'age': data["response"][0]["player"]["age"],
        'nationality': data["response"][0]["player"]["nationality"],
        'photo': data["response"][0]["player"]["photo"],
        'birth': data["response"][0]["player"]["birth"]["date"],
        'place': data["response"][0]["player"]["birth"]["place"],
        'country': data["response"][0]["player"]["birth"]["country"],
        'height': data["response"][0]["player"]["height"],
        'weight': data["response"][0]["player"]["weight"],
        'team': data["response"][0]["statistics"][0]["team"]["name"],
        'logo': data["response"][0]["statistics"][0]["team"]["logo"],
        'positions': data["response"][0]["statistics"][0]["games"]["position"]
    }

    context = {
        'playerId': id_player,
        'info': info,
        'statistics': statistics,
    }

    return render(request=request, template_name="player.html", context=context)


# VECI DEO KODA JE POZAJMLJEN OD KOLJE
# def team in views_kolja.py
def manager_team_display(request: HttpRequest, id_team):
    current_season = calculate_current_season()
    conn.request("GET", "/v3/teams?id=" + str(id_team), headers=headers)
    data = json.loads(conn.getresponse().read())
    conn.request("GET", "/v3/coachs?team=" + str(id_team), headers=headers)
    data2 = json.loads(conn.getresponse().read())
    leagues=[]
    conn.request("GET", "/v3/leagues?team=" + str(id_team), headers=headers)
    data3 = json.loads(conn.getresponse().read())
    for r in data3["response"]:
        leagues.append({
            "leagueId": r["league"]["id"],
            "leagueName": r["league"]["name"],
            "leagueLogo": r["league"]["logo"],
            "country": r["country"]["code"]
        })
    stats = []
    for l in leagues:
        conn.request("GET", f"/v3/teams/statistics?league={l.get('leagueId')}&season="
                     + str(current_season) + "&team=" + str(id_team), headers=headers)
        data4 = json.loads(conn.getresponse().read())
        stats.append({
            "leagueId": l.get("leagueId"),
            "leagueName": l.get("leagueName"),
            "leagueLogo": l.get("leagueLogo"),
            "leagueCountry": l.get("country"),
            "form": data4["response"]["form"],
            "homeplayed": data4["response"]["fixtures"]["played"]["home"],
            "awayplayed": data4["response"]["fixtures"]["played"]["away"],
            "totalplayed": data4["response"]["fixtures"]["played"]["total"],
            "homewins": data4["response"]["fixtures"]["wins"]["home"],
            "awaywins": data4["response"]["fixtures"]["wins"]["away"],
            "totalwins": data4["response"]["fixtures"]["wins"]["total"],
            "homedraws": data4["response"]["fixtures"]["draws"]["home"],
            "awaydraws": data4["response"]["fixtures"]["draws"]["away"],
            "totaldraws": data4["response"]["fixtures"]["draws"]["total"],
            "homeloses": data4["response"]["fixtures"]["loses"]["home"],
            "awayloses": data4["response"]["fixtures"]["loses"]["away"],
            "totalloses": data4["response"]["fixtures"]["loses"]["total"],
            "goalsforhome": data4["response"]["goals"]["for"]["total"]["home"],
            "goalsforaway": data4["response"]["goals"]["for"]["total"]["away"],
            "goalsfortotal": data4["response"]["goals"]["for"]["total"]["total"],
            "goalsagainsthome": data4["response"]["goals"]["against"]["total"]["home"],
            "goalsagainstaway": data4["response"]["goals"]["against"]["total"]["away"],
            "goalsagainsttotal": data4["response"]["goals"]["against"]["total"]["total"],
            "goalsaverageforhome": data4["response"]["goals"]["for"]["average"]["home"],
            "goalsaverageforaway": data4["response"]["goals"]["for"]["average"]["away"],
            "goalsaveragefortotal": data4["response"]["goals"]["for"]["average"]["total"],
            "goalsaverageagainsthome": data4["response"]["goals"]["against"]["average"]["home"],
            "goalsaverageagainstaway": data4["response"]["goals"]["against"]["average"]["away"],
            "goalsaverageagainsttotal": data4["response"]["goals"]["against"]["average"]["total"],
            "cleansheethome": data4["response"]["clean_sheet"]["home"],
            "cleansheetaway": data4["response"]["clean_sheet"]["away"],
            "cleansheettotal": data4["response"]["clean_sheet"]["total"],
            "penaltytotal": data4["response"]["penalty"]["total"],
            "penaltyscored": data4["response"]["penalty"]["scored"]["total"],
            "penaltymissed": data4["response"]["penalty"]["missed"]["total"],
        })

        conn.request("GET", "/v3/players/squads?team=" + str(id_team), headers=headers)
        data4 = json.loads(conn.getresponse().read())
        players = []
        if data4["response"][0]["players"]:
            for p in data4["response"][0]["players"]:
                players.append({
                    'playerId': p["id"],
                    'playerName': p["name"],
                    'playerAge': p["age"],
                    'playerPhoto': p["photo"],
                    'playerNumber': p["number"],
                    'playerPosition': p["position"]
                })

    context = {
        "name": data["response"][0]["team"]["name"],
        "id": id_team,
        "country": data["response"][0]["team"]["country"],
        "logo": data["response"][0]["team"]["logo"],
        "founded": data["response"][0]["team"]["founded"],
        "stadion": data["response"][0]["venue"]["name"],
        "city": data["response"][0]["venue"]["city"],
        "capacity": data["response"][0]["venue"]["capacity"],
        "coach": data2["response"][0]["name"],
        "nationality": data2["response"][0]["nationality"],
        "age": data2["response"][0]["age"],
        "coachphoto": data2["response"][0]["photo"],
        "stats": stats,
        "leagues": leagues,
        "players": players,
    }

    return render(request=request, template_name="team.html", context=context)
