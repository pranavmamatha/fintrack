from db.models import Expense, Category
from sqlalchemy import func

def add_expense(session, title, amount, date, category):
    cat = session.query(Category).filter_by(name=category).first()
    if not cat:
        cat = Category(name=category)
        session.add(cat)
        session.commit()

    exp = Expense(title=title, amount=amount, date=date, category_id=cat.id)
    session.add(exp)
    session.commit()
    print("Expense added.")


def update_expense(session, expense_id, title=None, amount=None):
    exp = session.get(Expense, expense_id)
    if not exp:
        print("Not found.")
        return

    if title:
        exp.title = title
    if amount:
        exp.amount = amount

    session.commit()
    print("Updated.")


def delete_expense(session, expense_id):
    exp = session.get(Expense, expense_id)
    if not exp:
        print("Not found.")
        return

    session.delete(exp)
    session.commit()
    print("Deleted.")
