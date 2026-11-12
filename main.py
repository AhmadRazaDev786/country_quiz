from api import fetch_countries
from quiz import prepare_country


def main():
    countries = fetch_countries()

    clean_countries = [
        prepare_country(country)
        for country in countries
        if country.get("names", {}).get("common")
    ]

    print(f"Loaded {len(clean_countries)} countries!")

    for country in clean_countries[:3]:
        print(country)


if __name__ == "__main__":
    main()
