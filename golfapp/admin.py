from django.contrib import admin
from .models import ShotPercentages

class ShotPercentagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShotPercentages, ShotPercentagesAdmin)
