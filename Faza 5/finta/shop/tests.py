from django.test import TestCase

# Create your tests here.
from shop.views_berke import *
from shop.views_slavko import diffTime


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


