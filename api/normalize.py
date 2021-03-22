
def normalize_most_expensive(data):
    response = []
    results = data.get('results', [])
    for r in results:
        response.append(
            {
                "title": r.get('title', ''),
                "price": r.get('price', ''),
                "link": r.get('permalink', '')
            }
        )

    return response
