from api import fetch_countries
from quiz import prepare_country, ask_capital_question


def play_round(countries):
    total_questions = 5
    score = 0

    print("\nStarting a new round!")

    for question_number in range(1, total_questions + 1):
        print(f"\nQuestion {question_number}/{total_questions}")

        is_correct = ask_capital_question(countries)

        if is_correct:
            score += 1

    print("\n" + "=" * 35)
    print(f"Your final score: {score}/{total_questions}")
    print("=" * 35)


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

    while True:
        play_round(clean_countries)

        while True:
            choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

            if choice in ("yes", "y"):
                break
            elif choice in ("no", "n"):
                print("\nThanks for playing!")
                return
            else:
                print("Please enter yes or no.")


if __name__ == "__main__":
    main()
