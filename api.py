import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REST_COUNTRIES_API_KEY")


def fetch_countries():
    if not API_KEY:
        print("API key not found. Check your .env file.")
        return []

    url = "https://api.restcountries.com/countries/v5"

    headers = {"Authorization": f"Bearer {API_KEY}"}

    params = {
        "limit": 100,
        "response_fields": "names.common,capitals,region,flag.emoji,currencies,languages",
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)

        response.raise_for_status()

        result = response.json()
        return result["data"]["objects"]

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return []

    except (KeyError, TypeError):
        print("Unexpected API response format.")
        return []
