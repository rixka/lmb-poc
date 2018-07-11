from os import environ
from flask import Blueprint, request, abort
from pymongo import MongoClient

from utils import (
    json_response, validate_object_id,
    parse_query, validate_rating
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

@api.route('/cupcakes/search', methods=['GET'])
def cupcakes_search():
    message = parse_query('message')

    if not message:
        return cupcakes_list()

    query = { '$text': { '$search': message } }
    cupcakes = list(db.cupcakes.find(query))
    check_not_empty(cupcakes)

    return json_response({
        'data': cupcakes
    })

@api.route('/cupcakes/rating', methods=['POST'])
def create_cupcakes_rating():
    data = request.json
    data['cupcakeId'] = validate_object_id(data['cupcakeId'])

    validate_rating(data['rating'])
    validate_cupcake_exists(data['cupcakeId'])

    rating_id = db.ratings.insert(data)
    headers = { 'Location': str.join('/', [ '/cupcakes/rating', str(rating_id) ]) }
    return json_response({ 'message': 'The item was created successfully' }, 201, headers)

@api.route('/cupcakes/rating/<rating_id>', methods=['GET'])
def cupcakes_rating(rating_id):
    rating_id = validate_object_id(rating_id)
    rating = list(db.ratings.find({ '_id': rating_id }).limit(1))
    check_not_empty(rating)

    return json_response({
        'data': rating[0]
    })

@api.route('/cupcakes/avg/rating/<cupcake_id>', methods=['GET'])
def cupcakes_avg_rating(cupcake_id):
    cupcake_id = validate_object_id(cupcake_id)
    validate_cupcake_exists(cupcake_id)

    rating = db.ratings.aggregate([
        {
            '$match': { 'cupcakeId': cupcake_id }
        },
        {
            '$group': {
                '_id': '$cupcakeId',
                'minRating': { '$min': '$rating' },
                'avgRating': { '$avg': '$rating' },
                'maxRating': { '$max': '$rating' }
            }
        }
    ])

    return json_response({
        'data': rating
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

# TODO: Move into a database module
def validate_cupcake_exists(cupcake_id):
    check_not_empty(
        list(
            db.cupcakes.find({ '_id': cupcake_id }, { '_id': 1 }).limit(1)
        )
    )

def check_not_empty(r):
    if r == []: abort(404)
