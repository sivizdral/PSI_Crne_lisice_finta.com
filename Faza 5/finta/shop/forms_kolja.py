from django.forms import Form, ModelForm
from django import forms


class SearchForm(Form):
    Search = forms.CharField(max_length=70)

class TeamS:
    name = ""
    logo = ""

    def __init__(self, n, l):
        name = n
        logo = l