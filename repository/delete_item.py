from repository.database import get_db


def delete_item(id):

    database = get_db()


    if database.execute(f"SELECT * FROM inventory WHERE id='{id}'").fetchone():
        database.execute(f"DELETE FROM inventory WHERE id='{id}'")
        database.commit()
        database.close()
        return True #{f"ID {id}":"deleted"}
    else:
        return False # {f"ID {id}":"not found"}
