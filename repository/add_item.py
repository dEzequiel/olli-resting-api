from repository.database import get_db


def add_item(name, sell_in, quality):
    database = get_db()

    item = [
        dict(row)
        for row in database.execute(
            "INSERT INTO inventory VALUES (?, ?, ?)", (name, sell_in, quality)
        )
    ]

    database.commit()
    database.close()
    return item
