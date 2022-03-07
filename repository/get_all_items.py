import sqlite3
from repository.database import get_db


def get_all_items():
    database = get_db()
    database.row_factory = sqlite3.Row
    cursor = database.cursor()

    r = cursor.execute('SELECT * FROM inventory')

    items = []
    for row in r.fetchall():
        items.append(dict(row))

    return items
