from os import environ
from flask import Blueprint, abort
from pymongo import MongoClient

from utils import (
    json_response, validate_object_id,
    parse_query
)

MONGO_HOST = environ.get('MONGO_HOST') or 'localhost'
MONGO_DB = environ.get('MONGO_DB') or 'development'

api = Blueprint('api', __name__)
db = MongoClient(MONGO_HOST, 27017)[MONGO_DB]


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    abort(404)

@api.route("/health")
def health():
    return json_response({'status': 'ok'}, 200)

@api.route('/cupcakes')
def cupcakes_list():
    last_id =  parse_query('last-id')
    query = { '_id': { '$gt': validate_object_id(last_id) } } if last_id else {}

    cupcakes = db.cupcakes.find(query).sort('_id').limit(5)
    return json_response({
        'data': cupcakes
    })

# === HANDLERS === #

@api.errorhandler(400)
def not_found(error):
    return json_response({'error': 'Bad Request'}, 400)

@api.errorhandler(404)
def not_found(error):
    return json_response({'error': 'Not Found'}, 404)

@api.errorhandler(500)
def internal_error(error):
    return json_response({'error': 'Internal Server Error'}, 500)

@api.errorhandler(501)
def not_implemented(error):
    return json_response({'error': 'Not Implemented'}, 501)

def check_not_empty(r):
    if r == []: abort(404)
