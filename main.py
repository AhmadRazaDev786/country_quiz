from api import fetch_countries
from quiz import prepare_country, ask_capital_question


def main():
    countries = fetch_countries()

    clean_countries = [
        prepare_country(country)
        for country in countries
        if country.get("names", {}).get("common")
    ]

    print("=" * 35)
    print("       WELCOME TO COUNTRY QUIZ")
    print("=" * 35)

    print(f"\nLoaded {len(clean_countries)} countries!")

    ask_capital_question(clean_countries)


if __name__ == "__main__":
    main()
