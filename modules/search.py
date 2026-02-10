from sqlalchemy import text

def search_by_date(session, date):
    sql = "SELECT title, amount FROM expenses WHERE date = :d"
    rows = session.execute(text(sql), {"d": date}).fetchall()

    for r in rows:
        print(r[0], "-", r[1])
