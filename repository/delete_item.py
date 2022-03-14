from repository.database import get_db

def delete_item(id):

    database = get_db()

    # Getting element just for testing purpose, also useful
    # to know which element was delete

    item = [
        dict(row)
        for row in database.execute(
            f"SELECT * FROM inventory WHERE id='{id}'"
        )
    ]

    database.execute(f"DELETE FROM inventory WHERE id='{id}'")
    database.commit()
    database.close()

    # The returned item is the deleted one
    return item