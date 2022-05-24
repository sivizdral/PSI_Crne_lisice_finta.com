from django.forms import Form, ModelForm
from django import forms

#Ceo ovaj fajl je napravio Konstantin Benovic 0114/2019

#Klasa (forma) koja sluzi za pretragu timova po imenu
class SearchForm(Form):
    Search = forms.CharField(max_length=70)
