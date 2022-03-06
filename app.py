from flask import Flask
from flask_restful import Resource, Api
from controller.item import Item
from controller.root import Root

app = Flask(__name__)

# API REST
api = Api(app, catch_all_404s=True)

api.add_resource(Root, "/")
api.add_resource(Item, "/item/<name>")

if __name__ == "__main__":
    app.run(debug=True)
