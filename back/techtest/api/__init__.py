from flask import Blueprint
from flask_restful import Api

from techtest.models.database import db
from techtest.errors import NotFoundError, NotValidError

from .characters import Characters, Character
from .clothes import Hats
from .data import Data

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    @api_bp.errorhandler(NotFoundError)
    def if_not_found(error):
        response = {
            "error": f"{error.resource} {error.resource_id} not found !!!"}
        return response, 404

    @ api_bp.errorhandler(NotValidError)
    def if_not_valid(error):
        response = {"error": f"{error.resource} {error.message}"}
        return response, 409

    api.add_resource(Characters, '/characters')
    api.add_resource(Character, '/character/<character_id>')
    api.add_resource(Hats, '/clothes/hats')
    api.add_resource(Data, '/data')

    app.register_blueprint(api_bp, url_prefix="/api/v1")
