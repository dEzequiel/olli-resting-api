import click
from flask import Blueprint, current_app
from repository.database import get_db

database_command = Blueprint("db", __name__)


def init_db():
    database = get_db()

    with current_app.open_resource("repository/sql_schema.sql") as f:
        database.executescript(f.read().decode("utf8"))


@database_command.cli.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database created")


def insert_db():
    database = get_db()

    with current_app.open_resource("repository/inserts.sql") as f:
        database.executescript(f.read().decode("utf8"))


@database_command.cli.command("insert-db")
def insert_db_command():
    insert_db()
    click.echo("Fields added to database")
