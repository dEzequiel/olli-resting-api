from flask import abort
from model.inventory import *

class Service():

    def get_object(self, name):

        if not name:
            abort(404, message="No object provided")

        if name in myjson.keys():
            return myjson[name], 201
        else:
            return f"{name} not in database"
