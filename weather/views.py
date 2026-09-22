from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import WeatherSnapshot
from .serializers import WeatherSnapshotSerializer

@api_view(['GET'])
def get_weather_snapshot(request):
    queryset = WeatherSnapshot.objects.all()
    serializer = WeatherSnapshotSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_weather_by_country(request, country_code):
    queryset = WeatherSnapshot.objects.filter(country_code=country_code)
    serializer = WeatherSnapshotSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
    