# FinTrack Pro – CLI Finance Manager

FinTrack Pro is a simple command-line tool to manage daily expenses.  
It uses **Python**, **SQLite**, and **SQLAlchemy ORM** for storing and managing data.

---

## Features
- Add expenses  
- Update expenses  
- Delete expenses  
- Search expenses by date  
- Category-wise spending report  
- Set monthly budget  
- Get alert when budget is exceeded  
- Data stored permanently in a local SQLite file  

---

## Project Structure
```
fintrack_pro/
│
├── app.py # Main CLI program
│
├── db/
│ ├── database.py # Database engine + Base
│ └── models.py # ORM models
│
├── modules/
│ ├── expenses.py # Add/Update/Delete expenses
│ ├── reports.py # Category analytics
│ ├── budgets.py # Budget handling
│ └── search.py # Search operations
│
└── requirements.txt
```

---

## Installation

### 1. Install dependencies
pip install -r requirements.txt


### 2. Run the application
python app.py


A SQLite database file (`fintrack.db`) will be created automatically.

---

## How to Use
When the app runs, a simple menu appears.  
Select a number to add an expense, update it, delete it, run a report, or check your budget.

The interface is beginner-friendly and fully terminal-based.

---

## Technologies Used
- Python  
- SQLite  
- SQLAlchemy ORM  

---

## Purpose
This project is ideal for beginners who want to learn:
- Python + databases  
- ORM basics  
- Simple CLI application structure  
- Writing clean and modular code  

---

## Note
Future enhancements like CSV export, authentication, or UI can be added later as needed.
