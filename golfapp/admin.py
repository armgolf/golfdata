from django.contrib import admin
from .models import Golfscore

class GolfscoreAdmin(admin.ModelAdmin):
    list_display = ['course', 'par1']

admin.site.register(Golfscore, GolfscoreAdmin)
