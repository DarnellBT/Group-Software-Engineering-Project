from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ['locationId', 'name', 'latitude', 'longitude']

admin.site.register(Location, LocationAdmin)