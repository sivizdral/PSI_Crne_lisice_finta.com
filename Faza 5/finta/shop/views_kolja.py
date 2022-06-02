from django.http import HttpRequest

import os
import http.client
import json

from django.shortcuts import render

#Ceo ovaj fajl je napravio Konstantin Benovic 0114/2019

from shop.forms_kolja import SearchForm
from shop.views_berke import *

#funkcija koja otvara html stranicu za odredjeni tim kome je prosledjen id tima
def team(request):
    '''

    :param request:Httprequest
    :return: render team.html stranica
    '''
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"

    str = "/v3/teams?id="+request.POST.get("id")
    conn.request("GET", str, headers=headers)

    data = json.loads(conn.getresponse().read())
    # = data["response"][0]["team"]["country"]
    str = "/v3/coachs?team=" + request.POST.get("id")
    conn.request("GET", str, headers=headers)
    data2 = json.loads(conn.getresponse().read())
    leagues=[]
    str = "/v3/leagues?team=" + request.POST.get("id")
    conn.request("GET", str, headers=headers)
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
        "/v3/teams/statistics?league=39&season=2021&team=33"
        str1 = f'/v3/teams/statistics?league={l.get("leagueId")}'
        str1+="&"
        str1+="season=2021&team="
        str1+=request.POST.get("id")
        #str = "/v3/statistics?league=" + l.get("leagueId")+"&season=2020&team="+request.POST.get("id")
        conn.request("GET", str1, headers=headers)
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

        str = "/v3/players/squads?team=" + request.POST.get("id")
        conn.request("GET", str, headers=headers)
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
        "id": request.POST.get("id"),
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
        "players": players
    }

    return render(request=request, template_name="team.html", context=context)

#funkcija koja otvara html stranicu za pretrazivanje timova po imenu
def teamsearch(request):
    '''

    :param request:Httprequest
    :return: render teamsearch.html stranica
    '''
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"

    form = SearchForm(request.POST or None)

    podaci = None
    if (form.is_valid()):
        str = "/v3/teams?search="+form.data.get("Search")
        conn.request("GET", str, headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        podaci = []
        for d in data["response"]:
            podaci.append({
                "name": d["team"]["name"],
                "logo": d["team"]["logo"],
                "id": d["team"]["id"]
            })
        if (len(podaci) > 6):
            podaci = podaci[:6]
        context = {
            "form": form,
            "data": podaci,
        }
        return render(request=request, template_name="searchteam.html", context=context)

    context = {
        "form": form,
        "data": podaci,
    }

    return render(request=request, template_name="searchteam.html", context=context)

#funcija koja otvara html stranicu za pregled pojedinacnog igraca, koji se trazi po svom idu
def player(request):
    '''
    :param request:Httprequest
    :return: render player.html stranica
    '''
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
    broj = request.POST.get("igrac")

    str = "/v3/players?id="+broj+"&season=2021"
    conn.request("GET", str, headers=headers)

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
        'playerId': broj,
        'info': info,
        'statistics': statistics,
    }

    return render(request=request, template_name="player.html", context=context)