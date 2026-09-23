from django.urls import path
from weather import views

urlpatterns = [
    path('', views.get_snapshots),
    path('snapshots', views.get_snapshots),
    path('<country_code>', views.get_weather_by_country)
]