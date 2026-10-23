@'
# FinTrack — Expense Tracker

A personal finance web application built with Django and PostgreSQL.

## Features

- Track income and expenses
- View total income, expenses, and current balance
- Visualize expenses with a doughnut chart
- Create, edit, and delete transactions
- Filter transactions by type and date range
- Search transactions by title
- Sort transactions by date or amount
- Organize transactions by category
- Dark-themed responsive interface
- Form validation

## Tech Stack

- Python
- Django
- PostgreSQL
- psycopg
- HTML, CSS, JavaScript
- Chart.js

## Requirements

- Python
- PostgreSQL
- pip

## Installation

1. Clone the repository:

   ```powershell
   git clone https://github.com/on3mor3t1m3/expense-tracker.git
   cd expense-tracker


2. Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\Activate.ps1
3. Install dependencies:
   python -m pip install -r requirements.txt
4. Create a .env file in the project root using .env.example as a template. Fill in your local Django and PostgreSQL settings.
5. Create a PostgreSQL database and user matching the values in .env.
6. Apply migrations:
   python manage.py migrate
7. Start the development server:
   python manage.py runserver
8. Open http://127.0.0.1:8000/ in your browser.
Environment Variables
The application uses a local .env file for configuration. See .env.example for the required variable names.

Never commit real passwords, secret keys, or other credentials.
Project Structure
expense-tracker/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── transactions/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── admin.py
├── .gitignore
├── manage.py
└── requirements.txt


Status
Personal portfolio project. Developed to practice Django, database integration, CRUD operations, filtering, and frontend development.
'@ | Set-Content -Encoding utf8 README.md
