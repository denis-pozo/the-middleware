from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import WeatherSnapshot

@api_view(['GET'])
def get_weather_snapshot(request):
    queryset = WeatherSnapshot.objects.all()
    serializer = WeatherSnapshotSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
    