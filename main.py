from db.database import Base, engine, SessionLocal
from modules.expenses import add_expense, update_expense, delete_expense
from modules.reports import category_report
from modules.budgets import set_budget, check_budget
from modules.search import search_by_date
from datetime import datetime

Base.metadata.create_all(bind=engine)

def main():
    session = SessionLocal()

    while True:
        print("\n--- FinTrack Pro ---")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. Category Report")
        print("5. Set Budget")
        print("6. Check Budget")
        print("7. Search by Date")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            title = input("Title: ")
            amount = float(input("Amount: "))
            date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d")
            category = input("Category: ")
            add_expense(session, title, amount, date, category)

        elif ch == "2":
            eid = int(input("Expense ID: "))
            title = input("New Title (blank=skip): ")
            amount = input("New Amount (blank=skip): ")
            update_expense(session, eid,
                           title if title else None,
                           float(amount) if amount else None)

        elif ch == "3":
            eid = int(input("Expense ID: "))
            delete_expense(session, eid)

        elif ch == "4":
            category_report(session)

        elif ch == "5":
            month = input("Month (1-12): ")
            limit = float(input("Limit: "))
            set_budget(session, month, limit)

        elif ch == "6":
            month = input("Month (1-12): ")
            check_budget(session, month)

        elif ch == "7":
            date = input("Date (YYYY-MM-DD): ")
            search_by_date(session, date)

        elif ch == "0":
            break

        else:
            print("Invalid.")

    session.close()


if __name__ == "__main__":
    main()
