import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = "repository/inventory.db"


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row

    return db


def close_connection(exception):
    db = get_db()
    if db is not None:
        db.close()


import click
from flask import Blueprint, current_app

database_test_command = Blueprint("test-db", __name__)


def init_db():
    database = get_db()

    with current_app.open_resource("repository/inventory_test/sql_schema.sql") as f:
        database.executescript(f.read().decode("utf8"))


@database_test_command.cli.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database created")


def insert_db():
    database = get_db()

    with current_app.open_resource("repository/inventory_test/inserts.sql") as f:
        database.executescript(f.read().decode("utf8"))


@database_test_command.cli.command("insert-db")
def insert_db_command():
    insert_db()
    click.echo("Fields added to database")


# Methods that interacts with the database. The ones used in tests/ and
# replicates the one used by original database.

def add_item(name, sell_in, quality):
    database = get_db()

    item = [
        dict(row)
        for row in database.execute(
            "INSERT INTO inventory_test VALUES (?, ?, ?, ?)", (None, name, sell_in, quality)
        )
    ]

    database.commit()
    database.close()
    return item


def delete_item(id):

    database = get_db()


    if database.execute(f"SELECT * FROM inventory WHERE id='{id}'").fetchone():
        database.execute(f"DELETE FROM inventory WHERE id='{id}'")
        database.commit()
        database.close()
        return True #{f"ID {id}":"deleted"}
    else:
        return False # {f"ID {id}":"not found"}

def get_all_items():
    database = get_db()
    items = [dict(row) for row in database.execute("SELECT * FROM inventory_test")]
    database.close()
    return items if len(items) != 0 else "Inventory is empty"


def get_item_by_quality(quality):

    database = get_db()
    item = [
        dict(row)
        for row in database.execute(
            f"SELECT * FROM inventory_test WHERE quality='{quality}'"
        )
    ]
    database.close()
    return item if len(item) != 0 else {f"Quality {quality}": "not found"}


def get_item_by_sell_in(sellin):
    database = get_db()
    item = [
        dict(row)
        for row in database.execute(f"SELECT * FROM inventory_test WHERE sell_in='{sellin}'")
    ]
    database.close()
    return item if len(item) != 0 else {f"Sell in {sellin}": "not found"}


def get_item(name):
    database = get_db()
    item = [
        dict(row)
        for row in database.execute(f"SELECT * FROM inventory_test WHERE name='{name}'")
    ]
    database.close()
    return item if len(item) != 0 else {name: "not found"}
