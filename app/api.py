from flask import Blueprint, abort
from utils import json_response

api = Blueprint('api', __name__)


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    abort(404)

@api.route("/health")
def health():
    return json_response({'status': 'ok'}, 200)


# === HANDLERS === #

@api.errorhandler(404)
def not_found(error):
    return json_response({'error': 'Not Found'}, 404)
