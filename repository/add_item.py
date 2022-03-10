from repository.database import get_db

def add_item(name, sell_in=10, quality=10):
    database = get_db()
    database.execute("INSERT INTO inventory (name, sell_in, quality) VALUES (?, ?, ?)", (name, sell_in, quality))
    database.commit()
    database.close()