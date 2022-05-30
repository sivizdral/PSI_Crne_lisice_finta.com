import datetime
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse

import os
import http.client
import json

@login_required(login_url='login')
def myprofile(request: HttpRequest):

    user = User.objects.get(pk=request.user.id)
    owns = Owns.objects.filter(username=user)
    articles_ids = []
    for o in owns:
        articles_ids.append(o.idarticle_id)

    articles = Article.objects.filter(idarticle__in=articles_ids)

    links = []
    enum = []
    cur = 0
    amount = []

    for article in articles:
        name = article.name.replace(' ', '_')
        if (os.path.exists(os.path.join(os.getcwd(), "shop\\static\\images\\" + name + ".svg"))):
            links.append("images/" + name + ".svg")
        else:
            links.append("images/" + name + ".png")

        enum.append(cur)
        cur = 1 - cur

        curAmount = Owns.objects.filter(username=user).filter(idarticle=article).first().amount
        amount.append(curAmount)

    artLink = zip(articles, links, enum, amount)

    context = {
        "artLink" : artLink,
        "links" : links,
        "owns" : owns,
        "articles" : articles,
        "day_joined" : request.user.date_joined.day,
        "month_joined" : request.user.date_joined.month,
        "year_joined" : request.user.date_joined.year,
    }
    return render(request, 'myprofile.html', context)

def diffTime(time1, time2):

    date_1 = f"{time1.day}/{time1.month}/{time1.year} {time1.hour}:{time1.minute}:{time1.second}"
    date_2 = f"{time2.day}/{time2.month}/{time2.year} {time2.hour}:{time2.minute}:{time2.second}"
    date_format_str = '%d/%m/%Y %H:%M:%S'
    start = datetime.datetime.strptime(date_2, date_format_str)
    end = datetime.datetime.strptime(date_1, date_format_str)

    difference = (end - start).total_seconds()

    return difference

def timeLeft(time1, time2):
    date_1 = f"{time1.day}/{time1.month}/{time1.year} {time1.hour}:{time1.minute}:{time1.second}" #now
    date_2 = f"{time2.day}/{time2.month}/{time2.year} {time2.hour}:{time2.minute}:{time2.second}" #registered
    date_format_str = '%d/%m/%Y %H:%M:%S'
    start = datetime.datetime.strptime(date_2, date_format_str)
    end = datetime.datetime.strptime(date_1, date_format_str)

    difference = (end - start).total_seconds()

    return difference

@login_required(login_url='login')
def finta_champs(request: HttpRequest):

    myUser = User.objects.get(pk=request.user.id)

    managerTeam = Managerteam.objects.filter(username=myUser.id).first()
    message = "get"

    needNewChampionship = False
    difference = 0;
    championship = None

    registered = False;

    if(len(Championship.objects.all()) != 0):
        lastEvent = Championship.objects.order_by("-time_started").first()

        dateNow = datetime.datetime.now()
        dateReg = lastEvent.time_started

        difference = diffTime(dateNow, dateReg)
        if(difference >= 1800): #half an hour
            needNewChampionship = True
        else:
            championship = lastEvent

    if(needNewChampionship):
        championship = Championship()
        championship.time_started = datetime.datetime.now()
        championship.name = "Championship " + str(championship.time_started.date()) + " - " + str(championship.time_started.hour) + ":" + str(championship.time_started.minute)
        championship.save()

    if(len(Championshipmanagerteam.objects.filter(idchampionship=championship).filter(idmanagerteam=managerTeam)) > 0):
        registered = True

    numberOfPlayers = len(Championshipmanagerteam.objects.filter(idchampionship=championship))

    previousChampionships = Championship.objects.exclude(idchampionship=championship.idchampionship).order_by('-time_started')

    # for champ in previousChampionships:
    #     playChampionship(champ)

    if(len(previousChampionships) > 0):
        champ = previousChampionships[0]
        if(champ.played == 0):
            playChampionship(champ)
            champ.played = 1
            champ.save()

    context = {
        "canPlay": managerTeam.count == 11,
        "diff": difference,
        "message": message,
        "registered": registered,
        "number" : numberOfPlayers,
        "previous" : previousChampionships,
    }

    if request.method == "POST":
        newParticipation = Championshipmanagerteam()
        newParticipation.idchampionship = championship
        newParticipation.idmanagerteam = managerTeam
        newParticipation.rank = -1
        newParticipation.save()

        return redirect('champs')



    return render(request, 'finta_champs.html', context)

def playGame(team1 : Managerteam, team2 : Managerteam):
    if(team1 == None): return team2;
    elif(team2 == None): return team1;

    sum = team1.overall + team2.overall

    rand = random.randint(0, sum)

    if(rand < team1.overall): return team1
    return team2

def playChampionship(championship : Championship):

    participants = Championshipmanagerteam.objects.filter(idchampionship=championship.idchampionship)

    for p in participants:
        user = User.objects.get(pk=p.idmanagerteam.username.id)
        user.appearances += 1
        user.save()

    indices = [0, 2, 1, 3]
    ind = 0
    quarters = [[], [], [], []]
    semis = [[], []]
    finals = []
    thirdplace = []

    for p in participants:
        quarters[indices[ind]].append(p.idmanagerteam)
        ind = (ind + 1) % 4

    for i in range(4):
        if(len(quarters[i]) != 2):
            quarters[i].append(None)
        if (len(quarters[i]) != 2):
            quarters[i].append(None)

    for i in range(4):
        semis[i // 2].append(playGame(quarters[i][0], quarters[i][1]))

    for i in range(2):
        team1 = semis[i][0]
        team2 = semis[i][1]
        winner = playGame(team1, team2)
        finals.append(winner)

        if winner == team1:
            thirdplace.append(team2)
        else:
            thirdplace.append(team1)


    #finals
    first = playGame(finals[0], finals[1])
    second = None
    if(finals[0] == first):
        second = finals[1]
    else:
        second = finals[0]
    third = playGame(thirdplace[0], thirdplace[1])

    if(len(participants.filter(idmanagerteam=first)) > 0):
        participant = participants.filter(idmanagerteam=first).first()
        participant.rank = 1
        participant.save()

        user = User.objects.get(pk=participant.idmanagerteam.username.id)
        user.gold += 1
        user.tokens += 500
        user.save()

    if (len(participants.filter(idmanagerteam=second)) > 0):
        participant = participants.filter(idmanagerteam=second).first()
        participant.rank = 2
        participant.save()

        user = User.objects.get(pk=participant.idmanagerteam.username.id)
        user.silver += 1
        user.tokens += 300
        user.save()

    if (len(participants.filter(idmanagerteam=third)) > 0):
        participant = participants.filter(idmanagerteam=third).first()
        participant.rank = 3
        participant.save()

        user = User.objects.get(pk=participant.idmanagerteam.username.id)
        user.bronze += 1
        user.tokens += 100
        user.save()


def seeChampionship(request: HttpRequest, id):

    first = None
    second = None
    third = None
    cnt = 0

    if(len(Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=1)) > 0):
        first = Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=1).first().idmanagerteam.name
    if (len(Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=2)) > 0):
        second = Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=2).first().idmanagerteam.name
    if (len(Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=3)) > 0):
        third = Championshipmanagerteam.objects.filter(idchampionship=id).filter(rank=3).first().idmanagerteam.name

    others = []
    all_participants = Championshipmanagerteam.objects.filter(idchampionship=id)
    cnt = len(all_participants)

    for part in all_participants:
        if(part.idmanagerteam.name != first and part.idmanagerteam.name != second and part.idmanagerteam.name != third):
            others.append(part.idmanagerteam.name)

    context = {
        "name" : Championship.objects.get(pk=id).name,
        "date" : Championship.objects.get(pk=id).time_started,
        "first" : first,
        "second" : second,
        "third" : third,
        "others" : others,
        "cnt" : cnt
    }

    return render(request, 'tournament_stats.html', context)

def champs_register(request: HttpRequest):
    return redirect('champs')

def ranklist(request: HttpRequest):

    users = User.objects.all()
    users = users.order_by('-gold', '-silver', '-bronze', 'appearances')
    context = {
        "users" : users,
    }

    return render(request, 'ranklist.html', context)