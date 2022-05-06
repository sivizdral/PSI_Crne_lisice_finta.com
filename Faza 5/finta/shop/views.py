from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group

import os

# Create your views here.

from django.http import HttpResponse

class Index(View):

    def post(self , request):
        return redirect('homepage')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/shop{request.get_full_path()[1:]}')


def shop(request):
    cartstring = request.POST.get('cartinput')
    if not cartstring:
        cartstring = ''
    cart = cartstring.split(',')
    cart = Article.objects.filter(name__in=cart)
    print('cart ', cart)
    articles = None
    types = Articletype.get_all_types()
    leagues = ["Bundesliga","Serie A","Premier league","LaLiga","Ligue 1","Superliga","Eredivisie"]
    typeID = request.GET.get('articletype')
    selectedLeagues = request.POST.getlist('leagueFilter')
    selectedTypes = request.POST.getlist('typeFilter')
    priceLow = request.POST.get('filterPriceLeft')
    priceHigh = request.POST.get('filterPriceRight')
    if (priceLow == None and priceHigh == None):
        priceLow = 0
        priceHigh = 1000
    else:
        priceLow = int(priceLow)
        priceHigh = int(priceHigh)
    firstLoad = 0
    articles = Article.get_all_articles_by_filters(selectedLeagues,selectedTypes,priceLow,priceHigh)
    art = Article.get_all_articles()
    print(articles)
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


    data = {}
    links = zip(links,articles)
    cartlinks = zip(cartlinks, art)
    data['articles'] = articles
    data['types'] = types
    data['leagues'] = leagues
    data['applied'] = "0"
    data['links'] = links
    #data['cart'] = cart
    data['cartlinks'] = cartlinks
    #data['cartstring'] = cartstring
    data['showcart'] = "1"
    print(links)

    print('you are : ', request.session.get('email'))
    return render(request, '../templates/shop.html', data)

def login_req(request):
    greska = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(User.objects.filter(username=username)) != 0:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, 'Succesful login')
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
    logout(request)
    return redirect('homepage')

def register(request):
    greska = ""
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        terms = request.POST.get('terms')

        if len(User.objects.filter(username=username)) != 0:
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
            user.save()
            group = Group.objects.get(name='default')
            user.groups.add(group)
            login(request, user)
            return redirect('homepage')
    context = {
        'greska': greska
    }
    return render(request, '../templates/register.html', context)