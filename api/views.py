from django.shortcuts import render

from .calls import get_publications_category
from .normalize import normalize_most_expensive


def biggest_sellers(request):
    return render(request, "biggest_sellers.html", {})


def most_expensive(request):
    response = get_publications_category("MLA420040", sort="price_desc", limit="50")
    normalize_data = normalize_most_expensive(response.json())
    return render(request, "most_expensive.html", {'result': {"list_items": normalize_data}})


def home(request):
    return render(request, "home.html", {})
