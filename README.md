# 🌍 Country Quiz

A Python-based terminal quiz game that tests your knowledge of countries around the world using live data from the REST Countries API.

The game asks multiple-choice questions about country capitals, tracks your score, and allows you to play multiple rounds.

## ✨ Features

- Fetches live country data from the REST Countries API.
- Processes and organizes country information.
- Generates random capital-related multiple-choice questions.
- Provides four answer options for each question.
- Validates user input.
- Tracks the score across five questions per round.
- Displays the final score.
- Allows users to play again.

## 🛠️ Technologies Used

- Python 3
- Requests
- REST Countries API
- python-dotenv
- Git and GitHub

## 📁 Project Structure

```text
country_quiz/
│
├── api.py              # Fetches country data from the API
├── quiz.py             # Processes data and handles quiz questions
├── main.py             # Main program and game flow
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from Git
├── .env                # Stores the API key (not committed)
└── README.md           # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AhmadRazaDev786/country_quiz.git
```

### 2. Navigate to the project directory

```bash
cd country_quiz
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your API key

Create a `.env` file in the project root directory:

```env
REST_COUNTRIES_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your own valid API key.

**Important:** Never share your API key or upload your `.env` file to GitHub.

### 6. Run the application

```bash
python main.py
```

## 🎮 Sample Output

```text
===================================
       WELCOME TO COUNTRY QUIZ
===================================

Loaded 100 countries!

Starting a new round!

Question 1/5

What is the capital of Armenia?

1. Yerevan
2. Pago Pago
3. Libreville
4. Tórshavn

Enter your answer (1-4): 1

Correct answer!

===================================
Your final score: 1/5
===================================

Do you want to play again? (yes/no):
```

*Note: The actual questions, answer options, and number of countries may vary depending on the API response.*

## 🌐 API Reference

This project uses the REST Countries API to retrieve country information, including:

- Country names
- Capital cities
- Currencies
- Languages
- Regions
- Flags

The API provides the live data used by the application.

## 🚀 Future Improvements

- Add currency-related questions.
- Add language-related questions.
- Add country flag identification questions.
- Add difficulty levels.
- Add a leaderboard to save high scores.

## 👨‍💻 Author

**Ahmad Raza**

- GitHub: [AhmadRazaDev786](https://github.com/AhmadRazaDev786)
- Project Repository: [Country Quiz](https://github.com/AhmadRazaDev786/country_quiz)

---

Built with Python as a practical project to explore API integration, data processing, and interactive terminal applications.