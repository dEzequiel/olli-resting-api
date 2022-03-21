from repository.database import get_db


def delete_item(id):

    database = get_db()

    # Getting element just for testing purpose, also useful
    # to know which element was delete

    item = [row for row in database.execute(f"SELECT * FROM inventory_test WHERE id='{id}'")]

    if len(item) == 0:
        return {f"ID {id}":"not found"}

    database.execute(f"DELETE FROM inventory_test WHERE id='{id}'")
    database.commit()
    database.close()

    return {f"ID {id}":"deleted"}
