
import sqlite3
from repository.database import get_db
from repository.get_all_items import get_all_items


def get_item_by_quality(quality):

    database = get_db()
    item = [dict(row) for row in database.execute(f"SELECT * FROM inventory WHERE quality='{quality}'")]
    database.close()
    return item if len(item) != 0 else {f"Quality {quality}":"not found"}

    # items = list(filter(lambda item: item['quality'] == quality, get_all_items()))
    # return items if len(items) != 0 else {quality:"not found"}
