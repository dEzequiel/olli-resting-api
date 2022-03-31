from repository.database import get_db


def delete_item(name):

    database = get_db()

    if database.execute(f"SELECT * FROM inventory WHERE name='{name}'").fetchone():
        database.execute(f"DELETE FROM inventory WHERE name='{name}'")
        database.commit()
        database.close()
        return True  # {f"ID {id}":"deleted"}
    else:
        return False  # {f"ID {id}":"not found"}
