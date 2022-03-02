from flask import Flask
from flask_restful import Resource
from model import inventory
from service.service import Service


class Object(Resource):

    def get(self, name):
        return Service.get_object(self.name), 200