
import sqlite3
from repository.database import get_db
from repository.get_all_items import get_all_items


def get_item_by_quality(quality):

    database = get_db()
    database.row_factory = sqlite3.Row
    cursor = database.cursor()

    r = cursor.execute(f'SELECT * from inventory WHERE quality={quality}')

    items = []
    for row in r.fetchall():
        items.append(dict(row))

    return items

    # items = list(filter(lambda item: item['quality'] == quality, get_all_items()))
    # return items if len(items) != 0 else {quality:"not found"}
