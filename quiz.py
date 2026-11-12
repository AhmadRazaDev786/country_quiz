import random


def prepare_country(country):
    """Extract useful information from a country API record."""

    capitals = country.get("capitals") or []
    currencies = country.get("currencies") or []
    languages = country.get("languages") or []

    return {
        "name": (country.get("names") or {}).get("common"),
        "capital": [item.get("name") for item in capitals if item.get("name")],
        "currency": [item.get("name") for item in currencies if item.get("name")],
        "languages": [item.get("name") for item in languages if item.get("name")],
        "region": country.get("region"),
        "flag": (country.get("flag") or {}).get("emoji"),
    }


def ask_capital_question(countries):
    """Ask the user to identify a country's capital."""

    # Keep countries that have a capital
    valid_countries = [country for country in countries if country["capital"]]

    # Select four countries with different capital names
    unique_countries = []
    seen_capitals = set()

    for country in valid_countries:
        capital = country["capital"][0]

        if capital not in seen_capitals:
            unique_countries.append(country)
            seen_capitals.add(capital)

    if len(unique_countries) < 4:
        print("Not enough countries to generate a question.")
        return False

    # Randomly select four countries
    options = random.sample(unique_countries, 4)

    # Select the correct answer
    correct_country = random.choice(options)
    correct_answer = correct_country["capital"][0]

    # Shuffle the options
    random.shuffle(options)

    print(f"\nWhat is the capital of {correct_country['name']}?")

    for index, country in enumerate(options, start=1):
        print(f"{index}. {country['capital'][0]}")

    # Get user's answer
    try:
        answer = int(input("\nEnter your answer (1-4): "))

        if answer not in range(1, 5):
            print("Please enter a number between 1 and 4.")
            return False

    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

    selected_answer = options[answer - 1]["capital"][0]

    if selected_answer == correct_answer:
        print("Correct answer!")
        return True

    print(f"Incorrect! The correct answer is {correct_answer}.")
    return False
