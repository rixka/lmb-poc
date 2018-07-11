from flask import Blueprint
from utils import json_response

api = Blueprint('api', __name__)


@api.route("/health")
def health():
    return json_response({'status': 'ok'}, 200)
