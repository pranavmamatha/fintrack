from db.models import Budget, Expense
from sqlalchemy import extract, func

def set_budget(session, month, limit):
    b = Budget(month=month, limit=limit)
    session.add(b)
    session.commit()
    print("Budget set.")


def check_budget(session, month):
    budget = session.query(Budget).filter_by(month=month).first()
    if not budget:
        print("No budget set.")
        return

    spent = (
        session.query(func.sum(Expense.amount))
        .filter(extract('month', Expense.date) == int(month))
        .scalar()
    ) or 0

    print("Spent:", spent, "Limit:", budget.limit)

    if spent > budget.limit:
        print("ALERT: Budget exceeded!")
