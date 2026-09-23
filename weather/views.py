from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from config import settings

from .clients.countries_client import CountryClient
from .clients.exceptions import CountryNotFoundError, CountryServiceError
from .models import CountrySnapshot
from .serializers import CountrySnapshotSerializer

countries_client = CountryClient(
    base_url=settings.COUNTRIES_BASE_URL,
    api_key=settings.COUNTRIES_API_KEY,
)

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

@api_view(['GET'])
def get_country_by_name(request, country_name):
    try:
        country_data = countries_client.get_by_country_name(country_name)
    except CountryNotFoundError:
        return Response({"detail": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
    except CountryServiceError:
        return Response({"detail": "Countries service unavailable"}, status=status.HTTP_502_BAD_GATEWAY)

    return Response(country_data)
    