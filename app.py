import sqlite3
from flask import Flask
from flask_restful import Resource, Api
from controller.add_item import AddItem
from controller.item import Item
from controller.items import Items
from controller.items_by_quality import ItemsByQuality
from controller.root import Root
from controller.items_by_sell_in import ItemsBySellin
from repository.commands import database_command
from repository.inventory_test.database_test import database_test_command

def create_app():
    app = Flask(__name__)

    # API REST
    api = Api(app, catch_all_404s=True)

    # Flask Blueprints encapsulate functionality, such as views, templates, and other resources.
    # A blueprint is a template for generating a "section" of a web application.
    app.register_blueprint(database_command)
    app.register_blueprint(database_test_command)


    api.add_resource(Root, "/")
    api.add_resource(Items, "/items")
    api.add_resource(Item, "/item/name/<name>")
    api.add_resource(ItemsBySellin, "/items/sellin/<sellin>")
    api.add_resource(ItemsByQuality, "/items/quality/<quality>")

    return app

if __name__ == "__main__":
    app.run(debug=True)
