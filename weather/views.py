from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import CountrySnapshot
from .serializers import CountrySnapshotSerializer

@api_view(['GET'])
def get_snapshots(request):
    queryset = CountrySnapshot.objects.all()
    serializer = CountrySnapshotSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_weather_by_country(request, country_code):
    queryset = CountrySnapshot.objects.filter(country_code=country_code)
    serializer = CountrySnapshotSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
    