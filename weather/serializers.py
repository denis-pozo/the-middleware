from rest_framework import serializers

class WeatherSnapshotSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=100)