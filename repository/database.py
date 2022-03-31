import sqlite3
from flask import g


DATABASE = "repository/inventory.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g.__database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# tierdown cerrar conexion
