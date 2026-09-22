from rest_framework import serializers

from .models import WeatherSnapshot

class WeatherSnapshotSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = WeatherSnapshot
        fields = ['country_code', 'name']