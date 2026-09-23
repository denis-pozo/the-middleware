from django.contrib import admin

from .models import CountrySnapshot

@admin.register(CountrySnapshot)
class CountrySnapshotAdmin(admin.ModelAdmin):
    list_display = ("name", "country_code", "capital", "temperature", "weather_description", "fetched_at", "created", "modified")
    list_filter = ("region", "country_code")
    search_fields = ("name", "country_code", "capital")
