from flask_restful import Resource

class Root(Resource):
    def get(self):
        return {"Welcome to":"Ollivanders Shop!"}, 200