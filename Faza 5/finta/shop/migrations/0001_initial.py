# Generated by Django 4.0.4 on 2022-05-09 13:48

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tokens', models.IntegerField(db_column='Tokens', default=0)),
                ('gold', models.IntegerField(db_column='Gold', default=0)),
                ('silver', models.IntegerField(db_column='Silver', default=0)),
                ('bronze', models.IntegerField(db_column='Bronze', default=0)),
                ('appearances', models.IntegerField(db_column='Appearances', default=0)),
                ('rank', models.IntegerField(db_column='Rank', default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('idarticle', models.AutoField(db_column='idArticle', primary_key=True, serialize=False)),
                ('image', models.FileField(db_column='Image', upload_to='images/')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('value', models.IntegerField(db_column='Value')),
                ('text', models.CharField(db_column='Text', max_length=255)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Articletype',
            fields=[
                ('idarticletype', models.AutoField(db_column='idArticleType', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
            ],
            options={
                'db_table': 'articletype',
            },
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('idchampionship', models.AutoField(db_column='idChampionship', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
            ],
            options={
                'db_table': 'championship',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('idleague', models.AutoField(db_column='idLeague', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('country', models.CharField(db_column='Country', max_length=255)),
            ],
            options={
                'db_table': 'league',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('idteam', models.AutoField(db_column='idTeam', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('country', models.CharField(db_column='Country', max_length=255)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('idplayer', models.AutoField(db_column='idPlayer', primary_key=True, serialize=False)),
                ('forename', models.CharField(db_column='Forename', max_length=255)),
                ('surname', models.CharField(db_column='Surname', max_length=255)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('country', models.CharField(db_column='Country', max_length=255)),
                ('position', models.CharField(db_column='Position', max_length=255)),
                ('idteam', models.ForeignKey(db_column='idTeam', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.team')),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='Participates',
            fields=[
                ('idparticipates', models.AutoField(db_column='idParticipates', primary_key=True, serialize=False)),
                ('idleague', models.ForeignKey(db_column='idLeague', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.league')),
                ('idteam', models.ForeignKey(db_column='idTeam', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.team')),
            ],
            options={
                'db_table': 'participates',
            },
        ),
        migrations.CreateModel(
            name='Owns',
            fields=[
                ('idowns', models.AutoField(db_column='idOwns', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(db_column='Amount')),
                ('idarticle', models.ForeignKey(db_column='idArticle', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.article')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'owns',
            },
        ),
        migrations.CreateModel(
            name='Managerteam',
            fields=[
                ('idmanagerteam', models.AutoField(db_column='idManagerTeam', primary_key=True, serialize=False)),
                ('offence', models.IntegerField(db_column='Offence')),
                ('defence', models.IntegerField(db_column='Defence')),
                ('value', models.IntegerField(db_column='Value')),
                ('overall', models.IntegerField(db_column='Overall')),
                ('rank', models.IntegerField(db_column='Rank')),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'managerteam',
            },
        ),
        migrations.CreateModel(
            name='Managerplays',
            fields=[
                ('idmanagerplays', models.AutoField(db_column='idManagerPlays', primary_key=True, serialize=False)),
                ('idmanagerteam', models.ForeignKey(db_column='idManagerTeam', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.managerteam')),
                ('idplayer', models.ForeignKey(db_column='idPlayer', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.player')),
            ],
            options={
                'db_table': 'managerplays',
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('idfixture', models.AutoField(db_column='idFixture', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='Date')),
                ('score', models.CharField(db_column='Score', max_length=255)),
                ('idteamaway', models.ForeignKey(db_column='idTeamAway', on_delete=django.db.models.deletion.DO_NOTHING, related_name='idTeamAway', to='shop.team')),
                ('idteamhome', models.ForeignKey(db_column='idTeamHome', on_delete=django.db.models.deletion.DO_NOTHING, related_name='idTeamHome', to='shop.team')),
            ],
            options={
                'db_table': 'fixture',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('idcomment', models.AutoField(db_column='idComment', primary_key=True, serialize=False)),
                ('text', models.CharField(db_column='Text', max_length=255)),
                ('idfixture', models.ForeignKey(db_column='idFixture', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.fixture')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Championshipmanagerteam',
            fields=[
                ('idchampionshipmanagerteam', models.AutoField(db_column='idChampionshipManagerTeam', primary_key=True, serialize=False)),
                ('rank', models.IntegerField(db_column='Rank')),
                ('idchampionship', models.ForeignKey(db_column='idChampionship', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.championship')),
                ('idmanagerteam', models.ForeignKey(db_column='idManagerTeam', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.managerteam')),
            ],
            options={
                'db_table': 'championshipmanagerteam',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='idarticletype',
            field=models.ForeignKey(db_column='idArticleType', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.articletype'),
        ),
    ]
