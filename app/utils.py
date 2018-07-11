from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import make_response, request, abort

JSON_MIME_TYPE = 'application/json'


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(dumps(data), status, headers)

def validate_object_id(_id):
    if ObjectId.is_valid(_id):
        return ObjectId(_id)
    else:
        abort(400)

def parse_query(param):
    target = dict(request.args).get(param)
    return target[0] if target else None

# Using jsonschema would be technically more accurate but this is faster
def validate_rating(n):
    if 1 <= n <= 5:
        return True

    abort(400)
