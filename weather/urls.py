from django.urls import path
from weather import views

urlpatterns = [
    path('', views.get_weather_snapshot),
    path('snapshot', views.get_weather_snapshot),
    path('<country_code>', views.get_weather_by_country)
]