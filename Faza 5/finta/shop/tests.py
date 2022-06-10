# Konstantin Benovic 0114/2019
# Slavko Krstic 0028/2019

from django.test import TestCase

# Create your tests here.
from .views_berke import *
from .views_slavko import diffTime
from .models import *
from django.contrib.auth.models import Group

class Test(TestCase):
    #testiranje uspesnosti pristupa timu
    def test_teamSuccess(self):
        uri = '/team/'
        response = self.client.post(uri, follow=True, data={
            "id": 33
        })

        self.assertContains(response, 'Manchester United', html=True)

    #testiranje neuspesnosti pristupa timu
    def test_teamFail(self):
        uri = '/team/'
        response = self.client.post(uri, follow=True, data={
            "id": 34
        })

        self.assertNotContains(response, 'Manchester United', html=True)

    # testiranje uspesnosti pristupa igracu
    def test_playerSuccess(self):
        uri = '/player/'
        response = self.client.post(uri, follow=True, data={
            "igrac": 276
        })

        self.assertContains(response, 'Neymar', html=True)

    # testiranje neuspesnosti pristupa igracu
    def test_playerFail(self):
        uri = '/player/'
        response = self.client.post(uri, follow=True, data={
            "igrac": 277
        })

        self.assertNotContains(response, 'Neymar', html=True)

    # testiranje uspesnosti pristupa postavi tima
    def test_teamSquadSuccess(self):
        uri = '/team/'
        response = self.client.post(uri, follow=True, data={
            "id": 33
        })

        self.assertContains(response, 'Players', html=True)

    # testiranje uspesnosti pristupa statistici tima
    def test_teamStatsSuccess(self):
        uri = '/team/'
        response = self.client.post(uri, follow=True, data={
            "id": 33
        })

        self.assertContains(response, 'Stats', html=True)

    # testiranje uspesnosti pristupa statistici igraca
    def test_playerStatisticsSuccess(self):
        uri = '/player/'
        response = self.client.post(uri, follow=True, data={
            "igrac": 276
        })

        self.assertContains(response, 'Statistics', html=True)

    # testiranje uspesnosti pronalaska tima u search-u
    def test_teamSerchSuccess(self):
        uri = '/teamsearch/'
        response = self.client.post(uri, follow=True, data={
            "Search": 'Manche'
        })

        self.assertContains(response, 'Manchester City', html = True)

    # testiranje uspesnosti pristupa pregleda meceva za odredjeni datum
    def test_fixturesSuccess(self):
        uri = '/fixtures/'
        response = self.client.post(uri, follow=True, data={
            "datum": "2022-05-07",
            "lige": 'all'
        })

        self.assertContains(response, "Date:", html=True)

    # testiranje neuspesnosti pretrage odredjene lige za odredjen datum
    def test_fixturesFail(self):
        uri = '/fixtures/'
        response = self.client.post(uri, follow=True, data={
            "datum": "2022-06-08",
            "lige": 'premier_league'
        })

        self.assertNotContains(response, "England - Premier League", html=True)

    #testiranje funkcije racunanja tekuce sezone
    def test_currentSeason(self):
        self.assertEqual(2021,calculate_current_season(),None)

    #testiranje pregleda profila
    def test_profilSuccess(self):
        newUser = User(username='toma', first_name='Tomislav', last_name='Benovic')
        newUser.set_password('P@ssw0rd123')
        newUser.save()
        self.client.login(username = 'toma', password='P@ssw0rd123')

        response = self.client.get("/myprofile/")

        self.assertContains(response, '@toma', html=True)

    # Uspesan login
    def test_login_successfully(self):
        user = User(username='toma')
        user.set_password('P@ssw0rd123')
        user.save()

        response = self.client.post("/login/", follow=True, data={
            'username' : 'toma',
            'password' : 'P@ssw0rd123',
        })

        self.assertContains(response, 'Logout', html=True)

    # Neuspesan login - ne postoji korisnik
    def test_login_unsuccessfully_user_dont_exist(self):

        response = self.client.post("/login/", follow=True, data={
            'username' : 'toma',
            'password' : 'P@ssw0rd123',
        })

        self.assertContains(response, 'This username does not exist!', html=True)

    # Neuspesan login - losa lozinka
    def test_login_unsuccessfully_bad_password(self):
        user = User(username='toma')
        user.set_password('P@ssw0rd123')
        user.save()

        response = self.client.post("/login/", follow=True, data={
            'username': 'toma',
            'password': 'Passw0rd123',
        })

        self.assertContains(response, 'The password is incorrect!', html=True)

    # Uspesna registracija
    def test_register_succesfully(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'Passw0rd123',
            'confirm' : 'Passw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'Logout', html=True)

    # Neuspesna registracija - prazno ime
    def test_register_unsuccesfully_empty_name(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : '',
            'surname' : 'Benovic',
            'password': 'Passw0rd123',
            'confirm' : 'Passw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'Name cannot be empty!', html=True)

    # Neuspesna registracija - prazno prezime
    def test_register_unsuccesfully_empty_surname(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : '',
            'password': 'Passw0rd123',
            'confirm' : 'Passw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'Surname cannot be empty!', html=True)

    # Neuspesna registracija - prazno korisnicko ime
    def test_register_unsuccesfully_empty_username(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': '',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'Passw0rd123',
            'confirm' : 'Passw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'Username cannot be empty!', html=True)

    # Neuspesna registracija - prazna lozinka
    def test_register_unsuccesfully_empty_password(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': '',
            'confirm' : 'Passw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'Password cannot be empty!', html=True)

    # Neuspesna registracija - lozinka mala slova
    def test_register_unsuccesfully_password_lowercase(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'PASSWORD123',
            'confirm' : 'PASSWORD123',
            'terms': 'on',
        })

        self.assertContains(response, 'Password must contain lowercase letters!', html=True)

    # Neuspesna registracija - lozinka velika slova
    def test_register_unsuccesfully_password_uppercase(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'p@ssword123',
            'confirm' : 'p@ssword123',
            'terms': 'on',
        })

        self.assertContains(response, 'Password must contain uppercase letters!', html=True)

    # Neuspesna registracija - lozinka brojevi
    def test_register_unsuccesfully_password_numbers(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'P@ssword',
            'confirm' : 'P@ssword',
            'terms': 'on',
        })

        self.assertContains(response, 'Password must contain numbers!', html=True)

    # Neuspesna registracija - lozinka mala duzina
    def test_register_unsuccesfully_password_length(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'P@ssw12',
            'confirm' : 'P@ssw12',
            'terms': 'on',
        })

        self.assertContains(response, 'Password must be at least 8 characters long!', html=True)

    # Neuspesna registracija - zauzeto ime
    def test_register_unsuccesfully_username_taken(self):
        group = Group(name='default')
        group.save()

        user = User(username='toma')
        user.set_password('P@ssw0rd123')
        user.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name' : 'Tomislav',
            'surname' : 'Benovic',
            'password': 'P@ssw0rd123',
            'confirm' : 'P@ssw0rd123',
            'terms': 'on',
        })

        self.assertContains(response, 'This username is already taken!', html=True)

    # Neuspesna registracija - nisu iste lozinke
    def test_register_unsuccesfully_confirmation(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name': 'Tomislav',
            'surname': 'Benovic',
            'password': 'P@ssw0rd123',
            'confirm': 'P@ssw0rd1234',
            'terms': 'on',
        })

        self.assertContains(response, 'The password and confirmation are not the same!', html=True)

    # Neuspesna registracija - nema potvrde
    def test_register_unsuccesfully_terms(self):
        group = Group(name='default')
        group.save()

        response = self.client.post("/register/", follow=True, data={
            'username': 'toma',
            'name': 'Tomislav',
            'surname': 'Benovic',
            'password': 'P@ssw0rd123',
            'confirm': 'P@ssw0rd123',
            'terms': '',
        })

        self.assertContains(response, 'You have to agree with terms and conditions!', html=True)

    # Uspesan logout
    def test_logout_successfully(self):
        user = User(username='toma')
        user.set_password('P@ssw0rd123')
        user.save()

        self.client.post("/login/", follow=True, data={
            'username': 'toma',
            'password': 'P@ssw0rd123',
        })

        response = self.client.post("/logout/", follow=True, data={})

        self.assertContains(response, 'Login', html=True)

    # Neuspesan ulaz na menadzera - autentifikacija
    def test_manager_authentication(self):
        response = self.client.get("/manager/", follow=True)

        self.assertContains(response, 'Please log in to your account', html=True)

    # Neuspesan ulaz na sampionat - autentifikacija
    def test_champs_authentication(self):
        response = self.client.get("/champs/", follow=True)

        self.assertContains(response, 'Please log in to your account', html=True)



