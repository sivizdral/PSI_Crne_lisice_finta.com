from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Article(models.Model):
    idarticle = models.AutoField(db_column='idArticle', primary_key=True)  # Field name made lowercase.
    image = models.FileField(upload_to='images/', db_column='Image')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.
    idarticletype = models.ForeignKey('Articletype', models.DO_NOTHING, db_column='idArticleType')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'article'

    @staticmethod
    def get_all_articles():
        return Article.objects.all()

    @staticmethod
    def get_all_articles_by_articletypeid(articletype_id):
        if articletype_id:
            return Article.objects.filter(idarticletype=articletype_id)
        else:
            return Article.get_all_articles();

    @staticmethod
    def get_all_articles_by_league(league_name):
        if league_name:
            return Article.objects.filter(text=league_name)
        else:
            return Article.get_all_articles();

    @staticmethod
    def get_all_articles_by_price(low,high):
        if (low and high):
            return Article.objects.filter(value__range=(low,high))
        else:
            return Article.get_all_articles();

    @staticmethod
    def get_all_articles_by_filters(leagueList,typeList,lowPrice,highPrice):
        articles = Article.get_all_articles_by_price(lowPrice,highPrice)
        for type in typeList:
            type = int(type)
        leagueList.append("")
        if (len(typeList) != 0):
            articles = articles.filter(idarticletype__idarticletype__in=typeList)
        if (len(leagueList) != 1):
            articles = articles.filter(text__in=leagueList)
        return articles


class Articletype(models.Model):
    idarticletype = models.AutoField(db_column='idArticleType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'articletype'

    @staticmethod
    def get_all_types():
        return Articletype.objects.all()


class Championship(models.Model):
    idchampionship = models.AutoField(db_column='idChampionship', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'championship'


class Championshipmanagerteam(models.Model):
    idchampionshipmanagerteam = models.AutoField(db_column='idChampionshipManagerTeam', primary_key=True)  # Field name made lowercase.
    idchampionship = models.ForeignKey(Championship, models.DO_NOTHING, db_column='idChampionship')  # Field name made lowercase.
    idmanagerteam = models.ForeignKey('Managerteam', models.DO_NOTHING, db_column='idManagerTeam')  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.

    class Meta:
        db_table = 'championshipmanagerteam'


class Comment(models.Model):
    idcomment = models.AutoField(db_column='idComment', primary_key=True)  # Field name made lowercase.
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')  # Field name made lowercase.
    idfixture = models.ForeignKey('Fixture', models.DO_NOTHING, db_column='idFixture')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'comment'


class Fixture(models.Model):
    idfixture = models.AutoField(db_column='idFixture', primary_key=True)  # Field name made lowercase.
    idteamhome = models.ForeignKey('Team', models.DO_NOTHING, related_name='idTeamHome', db_column='idTeamHome')  # Field name made lowercase.
    idteamaway = models.ForeignKey('Team', models.DO_NOTHING, related_name='idTeamAway', db_column='idTeamAway')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'fixture'


class League(models.Model):
    idleague = models.AutoField(db_column='idLeague', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'league'


class Managerplays(models.Model):
    idmanagerplays = models.AutoField(db_column='idManagerPlays', primary_key=True)  # Field name made lowercase.
    idmanagerteam = models.ForeignKey('Managerteam', models.DO_NOTHING, db_column='idManagerTeam')  # Field name made lowercase.
    idplayer = models.ForeignKey('Player', models.DO_NOTHING, db_column='idPlayer')  # Field name made lowercase.

    class Meta:
        db_table = 'managerplays'


class Managerteam(models.Model):
    idmanagerteam = models.AutoField(db_column='idManagerTeam', primary_key=True)  # Field name made lowercase.
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')  # Field name made lowercase.
    offence = models.IntegerField(db_column='Offence')  # Field name made lowercase.
    defence = models.IntegerField(db_column='Defence')  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.
    overall = models.IntegerField(db_column='Overall')  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'managerteam'


class Owns(models.Model):
    idowns = models.AutoField(db_column='idOwns', primary_key=True)  # Field name made lowercase.
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')  # Field name made lowercase.
    idarticle = models.ForeignKey(Article, models.DO_NOTHING, db_column='idArticle')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        db_table = 'owns'


class Participates(models.Model):
    idparticipates = models.AutoField(db_column='idParticipates', primary_key=True)  # Field name made lowercase.
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idTeam')  # Field name made lowercase.
    idleague = models.ForeignKey(League, models.DO_NOTHING, db_column='idLeague')  # Field name made lowercase.

    class Meta:
        db_table = 'participates'


class Player(models.Model):
    idplayer = models.AutoField(db_column='idPlayer', primary_key=True)  # Field name made lowercase.
    forename = models.CharField(db_column='Forename', max_length=255)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idTeam')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'player'


class Team(models.Model):
    idteam = models.AutoField(db_column='idTeam', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'team'


class User(AbstractUser):
    tokens = models.IntegerField(db_column='Tokens', default=0)  # Field name made lowercase.
    gold = models.IntegerField(db_column='Gold', default=0)  # Field name made lowercase.
    silver = models.IntegerField(db_column='Silver', default=0)  # Field name made lowercase.
    bronze = models.IntegerField(db_column='Bronze', default=0)  # Field name made lowercase.
    appearances = models.IntegerField(db_column='Appearances', default=0)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', default=0)  # Field name made lowercase.
    profile_picture = models.ImageField(db_column='Profile_picture', upload_to='profile_pictures/', null=True)
    tokens_given = models.IntegerField(db_column='Tokens_given', default=0)

    class Meta:
        db_table = 'user'

