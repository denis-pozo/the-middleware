from django.db import models
from model_utils.models import TimeStampedModel

class WeatherSnapshot(TimeStampedModel):
    country_code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    population = models.IntegerField()
    flag_url = models.CharField(max_length=100)
    temperature = models.IntegerField()
    weather_description = models.CharField(max_length=100)
    fetched_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "weather snapshot"
        verbose_name_plural = "weather snapshots"
        ordering = ["country_code"]
    def __str__(self)->str: 
        return self.name
