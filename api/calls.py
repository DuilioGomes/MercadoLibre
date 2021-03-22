import requests


def get_publications_category(category, sort=None, limit=50, site_id="MLA"):
    url = f"https://api.mercadolibre.com/sites/{site_id}/search"

    params = {
        "category": category,
        "sort": sort,
        "limit": limit
    }

    response = requests.request("GET", url, params=params)

    return response
