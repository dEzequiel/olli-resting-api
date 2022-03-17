from repository.database import get_db


def delete_item(id):

    database = get_db()

    # Getting element just for testing purpose, also useful
    # to know which element was delete

    item = [
        dict(row)
        for row in database.execute(f"SELECT * FROM inventory WHERE id='{id}'")
    ]

    if len(item) != 0:
        database.execute(f"DELETE FROM inventory WHERE id='{id}'")
        database.commit()
        database.close()
        return f"Item with id={id} was deleted"
    else:
        return f"Item with id={id} was not found"
