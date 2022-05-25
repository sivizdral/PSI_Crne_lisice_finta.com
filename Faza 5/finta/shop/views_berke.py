import datetime
import math

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.auth.decorators import login_required

import os
import http.client
import json

from .models import *

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


@login_required(login_url='login')
def manager(request: HttpRequest):
    players = [
        {"id": "", "realplayer": "", "pos": "GK", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "LWB", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "LCB", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "RCB", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "RWB", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "LM", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "CM", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "RM", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "LAM", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "RAM", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
        {"id": "", "realplayer": "", "pos": "SS", "photo": "", "name": "", "age": "", "realteam": "", "team": "", "teamlogo": "", },
    ]

    manager_teams = Managerteam.objects.filter(username__exact=request.user.id)
    if len(manager_teams) > 0:
        manager_team = manager_teams[len(manager_teams) - 1]
    else:
        manager_team = Managerteam(username=request.user, offence=0, defence=0, value=0,
                                   overall=0, rank=0, name=request.user)
        manager_team.save()

    managerplays = Managerplays.objects.filter(idmanagerteam__exact=manager_team)
    count = 0
    for i in range(len(managerplays)):
        for j in range(len(players)):
            if managerplays[i].idplayer.position == players[j]["pos"]:
                players[j]["id"] = managerplays[i].idplayer.idplayer
                players[j]["photo"] = managerplays[i].idplayer.photo
                players[j]["name"] = managerplays[i].idplayer.name
                players[j]["age"] = managerplays[i].idplayer.age
                players[j]["team"] = managerplays[i].idplayer.idteam.name
                players[j]["teamlogo"] = managerplays[i].idplayer.idteam.photo
                players[j]["realplayer"] = managerplays[i].idplayer.realid
                players[j]["realteam"] = managerplays[i].idplayer.idteam.realid
                count += 1
                break

    if request.method == "POST":
        manager_team.registered = 1
        manager_team.save()

    context = {
        "players": players,
        "manager_team": manager_team,
        "count": count,
    }
    return render(request=request, template_name="manager.html", context=context)


def manager_teams(request: HttpRequest, search):
    context = {
        "nesto": search,
    }
    return render(request=request, template_name="manager_players.html", context=context)





def manager_players(request: HttpRequest, position):
    players = None

    if request.method == "POST":
        search_name = request.POST.get("player")
        search_team = request.POST.get("player_team")

        conn.request("GET", "/v3/teams?search=" + search_team, headers=headers)
        teams = json.loads(conn.getresponse().read())["response"]

        players = []
        for i in range(min(len(teams), 15)):
            conn.request("GET", "/v3/players?team=" + str(teams[i]["team"]["id"]) +
                         "&search=" + search_name, headers=headers)
            players.extend(json.loads(conn.getresponse().read())["response"])
        players = players[:15]
    context = {
        "position": position,
        "players": players,
    }
    return render(request=request, template_name="manager_players.html", context=context)


def manager_player_add(request: HttpRequest, position, id_player):
    manager_teams = Managerteam.objects.filter(username__exact=request.user.id)
    if len(manager_teams) > 0:
        manager_team = manager_teams[len(manager_teams) - 1]
    else:
        manager_team = Managerteam(username=request.user, offence=0, defence=0, value=0,
                                   overall=0, rank=0, name=request.user)
        manager_team.save()

    conn.request("GET", "/v3/players?id=" + str(id_player) + "&season=" +
                 str(calculate_current_season()), headers=headers)
    try:

        player = json.loads(conn.getresponse().read())["response"][0]

        try:
            players_team = Team(name=player["statistics"][0]["team"]["name"],
                country="",
                photo=player["statistics"][0]["team"]["logo"],
                realid=player["statistics"][0]["team"]["id"])
            players_team.save()
            manager_player = Player(forename=player["player"]["firstname"], surname=player["player"]["lastname"],
                name=player["player"]["name"], country=player["player"]["birth"]["country"],
                position=position, age=player["player"]["age"], photo=player["player"]["photo"],
                idteam=players_team, realid=player["player"]["id"])
        except:
            manager_player = Player(forename="", surname="", name=player["player"]["name"], country="",
                position=position, age=player["player"]["age"], photo=player["player"]["photo"],
                idteam=Team.objects.get(pk=1), realid=player["player"]["id"])

        manager_player.save()

        calculate_stats(position, player, manager_team, manager_player)

        manager_team.count += 1
        manager_team.save()

        managerplays = Managerplays(idmanagerteam=manager_team, idplayer=manager_player)
        managerplays.save()
    except:
        pass
    return render(request=request, template_name="manager_player_add.html", context={})


def calculate_stats(position, player, manager_team, manager_player):
    offence = 0
    defence = 0
    overall = 0
    value = 0
    try:
        stats = player["statistics"][0]
        if position == "LAM" or position == "RAM" or position == "SS":
            offence += stats["goals"]["total"] * 3
            offence += stats["goals"]["assists"]
            offence += math.floor(stats["shots"]["on"] * 10 / stats["shots"]["total"])
        elif position == "LM" or position == "CM" or position == "RM":
            offence += math.floor(stats["passes"]["key"] / 10)
            defence += math.floor(stats["passes"]["total"] / 30)
        elif position == "LWB" or position == "LCB" or position == "RCB" or position == "RWB":
            defence += stats["tackles"]["total"]
            defence += math.floor(stats["duels"]["won"] * 20 / stats["duels"]["total"])
        elif position == "GK":
            if stats["goals"]["saves"]:
                defence += math.floor(stats["goals"]["saves"] * 3 / 4)
            else:
                defence += 1

        overall += offence + defence - stats["cards"]["yellow"] - stats["cards"]["red"] * 2
        value += math.floor(stats["games"]["minutes"] / 10)
    except:
        offence += 1
        defence += 1
        overall += 1
        value += 10

    manager_team.offence += offence
    manager_team.defence += defence
    manager_team.overall += overall
    manager_team.value += value
    manager_team.save()

    manager_player.offence = offence
    manager_player.defence = defence
    manager_player.overall = overall
    manager_player.value = value
    manager_player.save()


def manager_player_remove(request: HttpRequest, id_player):
    managerplays = Managerplays.objects.filter(idplayer__idplayer__exact=id_player)
    player = Player.objects.get(pk=id_player)
    team = Team.objects.filter(idteam__exact=player.idteam.idteam)
    managerteam = Managerteam.objects.filter(username__exact=request.user)[0]

    managerteam.offence -= player.offence
    managerteam.defence -= player.defence
    managerteam.overall -= player.overall
    managerteam.value -= player.value
    managerteam.registered = 0
    managerteam.count -= 1
    managerteam.save()

    managerplays.delete()
    player.delete()
    team.delete()
    return render(request=request, template_name="manager_player_remove.html", context={})


def manager_standings(request: HttpRequest):
    data = []

    users = User.objects.all()
    for u in users:
        manager_teams = Managerteam.objects.filter(username__exact=u.id)
        if len(manager_teams) > 0:
            manager_team = manager_teams[len(manager_teams) - 1]
        else:
            manager_team = Managerteam(username=u, offence=0, defence=0, value=0,
                                       overall=0, rank=0, name=u)
            manager_team.save()

        data.append({
            "user": u.username,
            "players": manager_team.count,
            "value": manager_team.value,
            "overall": manager_team.overall,
        })

    data.sort(key=lambda x: x["overall"], reverse=True)

    data = data[:100]

    context = {
        "data": data,
    }

    return render(request=request, template_name="manager_standings.html", context=context)










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
