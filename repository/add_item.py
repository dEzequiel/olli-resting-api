from repository.database import get_db

def add_item(name, sell_in, quality):
    database = get_db()

    item = [dict(row) for row in database.execute("INSERT INTO inventory (name, sell_in, quality) VALUES (?, ?, ?)", (name, sell_in, quality))]

    database.commit()
    return item