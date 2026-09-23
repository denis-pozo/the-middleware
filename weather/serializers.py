from rest_framework import serializers

from .models import CountrySnapshot

class CountrySnapshotSerializer(serializers.ModelSerializer):
    model = CountrySnapshot

    class Meta:
        model = CountrySnapshot
        fields = '__all__'