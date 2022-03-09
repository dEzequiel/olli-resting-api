from repository.database import get_db
from repository.get_all_items import get_all_items


def get_item(name):
    database = get_db()
    item = [
        dict(row)
        for row in database.execute(f"SELECT * FROM inventory WHERE name='{name}'")
    ]
    database.close()
    return item if len(item) != 0 else {name: "not found"}
