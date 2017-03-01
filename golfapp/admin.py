from django.contrib import admin
from .models import ShotPercentages, Golfscore, TotalScores

class ShotPercentagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShotPercentages, ShotPercentagesAdmin)

class GolfscoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Golfscore, GolfscoreAdmin)

class TotalScoresAdmin(admin.ModelAdmin):
    pass

admin.site.register(TotalScores, TotalScoresAdmin)
