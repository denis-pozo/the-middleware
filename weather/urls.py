from django.urls import path
from weather import views

urlpatterns = [
    path('', views.get_snapshots),
    path('snapshots', views.get_snapshots),
    path('countries/<country_name>', views.get_country_by_name)
]