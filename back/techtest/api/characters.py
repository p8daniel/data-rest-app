import json

from flask import request
from flask_restful import Resource

from techtest.managers.characters import read_characters, \
    get_character_by_id, create_character, delete_character, \
    update_character, check_character


class Characters(Resource):
    def get(self):
        characters = [character.get_small_data() for character in
                      read_characters()]
        return characters

    def post(self):
        name = request.args['name']
        age = request.args['age']
        weight = request.args['weight']
        human = request.args['human'] == 'true'
        hat = request.args.get('hat')
        check_character(name, age, weight, human, hat)
        character = create_character(name, age, weight, human, hat)
        return character.get_small_data()


class Character(Resource):
    def get(self, character_id):
        character = get_character_by_id(character_id)
        return character.get_small_data()

    def delete(self, character_id):
        delete_character(character_id)

    def patch(self, character_id):
        data = {}
        for parameter, value in request.args.items():
            if parameter == 'human':
                data[parameter] = json.loads(value.lower())
            else:
                data[parameter] = value

        character = get_character_by_id(character_id)
        check_data = character.get_small_data()
        del check_data['id']
        if check_data['hat'] is not None:
            check_data['hat'] = character.hat.color
        for parameter, value in data.items():
            if parameter in check_data:
                check_data[parameter] = value
        check_character(**check_data)

        for parameter, value in data.items():
            update_character(character_id, parameter, value)

        return get_character_by_id(character_id).get_small_data()
