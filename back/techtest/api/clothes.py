from flask_restful import Resource

from techtest.managers.clothes import read_hats


class Hats(Resource):
    def get(self):
        hats = [hat.get_small_data() for hat in read_hats()]
        return hats
