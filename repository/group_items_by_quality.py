import sqlite3
from repository.database import get_db


def group_items_by_quality(quality):

    database = get_db()
    item = [
        dict(row)
        for row in database.execute(
            f"SELECT * FROM inventory WHERE quality='{quality}'"
        )
    ]
    database.close()
    return item if len(item) != 0 else {f"Quality {quality}": "not found"}
