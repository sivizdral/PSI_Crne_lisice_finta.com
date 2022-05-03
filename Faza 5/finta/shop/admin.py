from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Fixture)
admin.site.register(League)
admin.site.register(Participates)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Article)
admin.site.register(Articletype)
admin.site.register(Championship)
admin.site.register(Championshipmanagerteam)
admin.site.register(Comment)
admin.site.register(Managerteam)
admin.site.register(Managerplays)
admin.site.register(Owns)
admin.site.register(Role)
admin.site.register(User)