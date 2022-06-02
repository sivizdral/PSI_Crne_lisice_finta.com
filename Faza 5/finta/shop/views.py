# Ivan Cvetic, 2019/0183

import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group
from django.http import HttpRequest
import http.client
import json
import re

import os

# Create your views here.

from django.http import HttpResponse, HttpRequest


class Index(View):

    def post(self , request):
        '''
        Funkcija koja preusmerava pocetni zahtev na stranicu za utakmice
        :param request:HttpRequest
        :return:HttpResponseRedirect
        '''
        return redirect('homepage')

    def get(self , request):
        '''
        Funkcija koja preusmerava pocetni zahtev na stranicu za utakmice
        :param request:HttpRequest
        :return:HttpResponseRedirect
        '''
        # print()
        return HttpResponseRedirect(f'/fixtures{request.get_full_path()[1:]}')

@login_required(login_url='login')
def shop(request):
    '''
    Funkcija obradjuje zahtev korisnika kada udje u prodavnicu. Korisnik je poziva prvi put kada udje u prodavnicu, ali i kada kupi nesto u njoj.
    :param request:HttpRequest
    :return:HttpResponse
    '''
    cartstring = request.POST.get('cartstr')
    print(cartstring)
    if not cartstring:
        cartstring = ''
    cart = cartstring.split(',')
    cart = Article.objects.filter(name__in=cart)
    print('cart ', cart)
    articles = None
    types = Articletype.get_all_types()
    leagues = ["Bundesliga","Serie A","Premier league","LaLiga","Ligue 1","Superliga","Eredivisie"]
    articles = Article.get_all_articles()
    art = Article.get_all_articles()
    links = []
    cartlinks = []
    for article in articles:
        name = article.name.replace(' ', '_')
        if (os.path.exists(os.path.join(os.getcwd(),"shop\\static\\images\\"+name+".svg"))):
            links.append("images/"+name+".svg")
            cartlinks.append("images/" + name + ".svg")
        else:
            links.append("images/" + name + ".png")
            cartlinks.append("images/" + name + ".png")

    myuser = User.objects.get(pk=request.user.id)
    tokens = myuser.tokens

    for product in cart:
        if (len(Owns.objects.filter(username=myuser).filter(idarticle=product)) == 0):
            tokens -= product.value
            myuser.tokens = tokens
            myuser.save()
            owns = Owns()
            owns.idarticle = product
            owns.username = myuser
            owns.amount = 1
            owns.save()

    cart = []


    data = {}
    links = zip(links,articles)
    cartlinks = zip(cartlinks, art)

    data['articles'] = articles
    data['types'] = types
    data['leagues'] = leagues
    data['applied'] = "0"
    data['links'] = links
    data['tokens'] = tokens
    data['cartlinks'] = cartlinks
    return render(request, '../templates/shop.html', data)

def change_coins(request: HttpRequest):
    '''
    Funkcija se poziva da bi korisnik na osnovu datuma i logovanja dobio dodatne tokene.
    :param request: HttpRequest
    :return: HttpResponse
    '''
    myuser = User.objects.get(pk = request.user.id)

    dateNow = datetime.datetime.now()
    dateReg = myuser.date_joined
    date_1 = f"{dateNow.day}/{dateNow.month}/{dateNow.year} {dateNow.hour}:{dateNow.minute}:{dateNow.second}"
    date_2 = f"{dateReg.day}/{dateReg.month}/{dateReg.year} {dateReg.hour}:{dateReg.minute}:{dateReg.second}"
    date_format_str = '%d/%m/%Y %H:%M:%S'
    start = datetime.datetime.strptime(date_2, date_format_str)
    end = datetime.datetime.strptime(date_1, date_format_str)

    difference = (end - start).total_seconds()

    need_to_have = int(difference // (60 * 60 * 24)) * 100;
    have = myuser.tokens_given

    myuser.tokens_given = need_to_have
    myuser.tokens += need_to_have - have;
    myuser.save()

def login_req(request):
    '''
    Funckija se poziva kada korisnik pokusa da se uloguje na sistem.
    :param request: HttpRequest
    :return: HttpResponse
    '''
    greska = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(User.objects.filter(username=username)) != 0:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, 'Succesful login')
                change_coins(request)
                return redirect('homepage')
            else:
                greska = "The password is incorrect!"
        else:
            greska = "This username does not exist!"
    context = {
        "greska": greska
    }
    return render(request, '../templates/login.html', context)

def logout_req(request):
    '''
    Funkcija se poziva kada korisnik zeli da se izloguje iz sistema.
    :param request: HttpRequest
    :return: HttpResponse
    '''
    logout(request)
    return redirect('homepage')

def register(request):
    '''
    Funckija se poziva kada korisnik zeli da se registruje na sistem.
    :param request: HttpRequest
    :return: HttpResponse
    '''
    greska = ""
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        terms = request.POST.get('terms')
        picture = request.FILES.get('picture')
        print(picture)

        if len(name) == 0:
            greska = "Name cannot be empty!"
        elif len(surname) == 0:
            greska = "Surname cannot be empty!"
        elif len(username) == 0:
            greska = "Username cannot be empty!"
        elif len(password) == 0:
            greska = "Password cannot be empty!"
        elif not re.search("[a-z]", password):
            greska = "Password must contain lowercase letters!"
        elif not re.search("[A-Z]", password):
            greska = "Password must contain uppercase letters!"
        elif not re.search("[0-9]", password):
            greska = "Password must contain numbers!"
        elif len(password) < 8:
            greska = "Password must be at least 8 characters long!"
        elif len(User.objects.filter(username=username)) != 0:
            greska = "This username is already taken!"
        elif password != confirm:
            greska = "The password and confirmation are not the same!"
        elif terms != 'on':
            greska = "You have to agree with terms and conditions!"
        else:
            user = User()
            user.username = username
            user.password = make_password(password)
            user.first_name = name
            user.last_name = surname
            user.tokens = 0
            user.tokens_given = 0
            user.save()
            group = Group.objects.get(name='default')
            user.groups.add(group)
            login(request, user)
            return redirect('homepage')
    context = {
        'greska': greska
    }
    return render(request, '../templates/register.html', context)


conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
headers = {
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com",
    'X-RapidAPI-Key': "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
}

leagues = {
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

def stats(request):
    '''
    Funckija se poziva kada se korisnik pozicionira na stranicu stats i vraca mu statistike na osnovu njegovog izbora vrednosti.
    :param request: HttpRequest
    :return: HttpResponse
    '''
    data_host = "api-football-v1.p.rapidapi.com"
    data_key = "ebad167f98mshfc189ed1132c723p189e18jsn516eb7007a02"
    data_refresh = "3600"
    data_team = ""
    data_league = "39"
    data_season = "2020"

    if request.method == "POST":
        data_league = leagues[request.POST.get("league")]
        data_team = request.POST.get('team')
        data_season = str(request.POST.get('season'))
        if (len(data_team) > 1):
            link = "/v3/teams?search=" + data_team
            conn.request("GET", link, headers=headers)
            res = conn.getresponse()
            data = res.read()
            data = json.loads(data)
            data_team = data["response"][0]["team"]["id"]

    context = {
        "data_host": data_host,
        "data_key": data_key,
        "data_team": data_team,
        "data_league": data_league,
        "data_season": data_season
    }

    return render(request,'stats.html', context)