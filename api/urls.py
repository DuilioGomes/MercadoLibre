from django.urls import path

from .views import biggest_sellers, most_expensive, home

urlpatterns = [
    path('biggest_sellers/', biggest_sellers),
    path('most_expensive/', most_expensive),
    path('', home),
]
