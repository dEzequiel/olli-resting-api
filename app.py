import sqlite3
from flask import Flask
from flask_restful import Resource, Api
from controller.item import Item
from controller.items import Items
from controller.items_by_quality import ItemsByQuality
from controller.root import Root
from controller.items_by_sell_in import ItemsBySellin
from repository.get_all_items import get_all_items
from repository.get_item import get_item


app = Flask(__name__)

# API REST
api = Api(app, catch_all_404s=True)

api.add_resource(Root, "/")
api.add_resource(Items, "/items")
api.add_resource(Item, "/item/name/<name>")
api.add_resource(ItemsBySellin, "/items/sellin/<sellin>")
api.add_resource(ItemsByQuality, "/items/quality/<quality>")

if __name__ == "__main__":
    app.run(debug=True)
