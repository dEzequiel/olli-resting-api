import sqlite3
from flask import Flask
from flask_restful import Resource, Api
from controller.add_item import AddItem
from controller.item import Item
from controller.items import Items
from controller.items_by_quality import ItemsByQuality
from controller.root import Root
from controller.items_by_sell_in import ItemsBySellin


app = Flask(__name__)

# API REST
api = Api(app, catch_all_404s=True)

api.add_resource(Root, "/")
api.add_resource(Items, "/items")
api.add_resource(Item, "/item/name/<name>")
api.add_resource(ItemsBySellin, "/items/sellin/<sellin>")
api.add_resource(ItemsByQuality, "/items/quality/<quality>")
api.add_resource(AddItem, "/item/add/<name>")

if __name__ == "__main__":
    app.run(debug=True)
