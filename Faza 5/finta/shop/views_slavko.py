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

import os
import http.client
import json

@login_required(login_url='login')
def myprofile(request: HttpRequest):
    context = {
        "day_joined" : request.user.date_joined.day,
        "month_joined" : request.user.date_joined.month,
        "year_joined" : request.user.date_joined.year,
    }
    return render(request, 'myprofile.html', context)