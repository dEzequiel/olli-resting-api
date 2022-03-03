from flask import Flask
from flask_restful import Resource
from repository import inventory
from service.get_object import Service


class Object(Resource):

    def get(self, name):
        return Service.get_object(self.name), 200