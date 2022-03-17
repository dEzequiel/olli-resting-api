import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = "repository/inventory.db"

def get_db():
    db = sqlite3.connect(DATABASE)
    return db


def close_connection(exception):
    db = get_db()
    if db is not None:
        db.close()


import click
from flask import Blueprint, current_app

database_test_command = Blueprint('test-db', __name__)

def init_db():
    database = get_db()

    with current_app.open_resource('repository/inventory_test/sql_schema.sql') as f:
        database.executescript(f.read().decode('utf8'))

@database_test_command.cli.command('init-db')
def init_db_command():
    init_db()
    click.echo("Database created")

def insert_db():
    database = get_db()

    with current_app.open_resource('repository/inventory_test/inserts.sql') as f:
        database.executescript(f.read().decode('utf8'))

@database_test_command.cli.command('insert-db')
def insert_db_command():
    insert_db()
    click.echo("Fields added to database")
