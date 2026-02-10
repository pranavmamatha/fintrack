from sqlalchemy import text

def category_report(session):
    sql = """
    SELECT c.name, SUM(e.amount)
    FROM categories c
    JOIN expenses e ON c.id = e.category_id
    GROUP BY c.name;
    """
    rows = session.execute(text(sql)).fetchall()

    for r in rows:
        print(r[0], ":", r[1])
