from flask_restful import Resource
from flask import request

from techtest.managers.data import store_data_to_db


class Data(Resource):
    def post(self):
        data = request.json
        store_data_to_db(data, 'json')
        return True
