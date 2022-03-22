from repository.database import get_db


def delete_item(id):

    database = get_db()


    if database.execute(f"SELECT * FROM inventory_test WHERE id='{id}'").fetchone():
        database.execute(f"DELETE FROM inventory_test WHERE id='{id}'")
        database.commit()
        database.close()
        return {f"ID {id}":"deleted"}
    else:
        return {f"ID {id}":"not found"}
