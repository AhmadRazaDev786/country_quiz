def prepare_country(country):
    """Extract useful information from a country API record."""

    name = (country.get("names") or {}).get("common")

    capitals = country.get("capitals") or []
    currencies = country.get("currencies") or []
    languages = country.get("languages") or []

    return {
        "name": name,
        "capital": [item.get("name") for item in capitals if item.get("name")],
        "currency": [item.get("name") for item in currencies if item.get("name")],
        "languages": [item.get("name") for item in languages if item.get("name")],
        "region": country.get("region"),
        "flag": (country.get("flag") or {}).get("emoji"),
    }
