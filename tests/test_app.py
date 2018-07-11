import pytest

from flask import url_for
from app import utils


class TestApp(object):
    def test_health(self, accept_json, client):
        res = client.get(url_for('api.health'), headers=accept_json)
    
        assert res.status_code == 200
        assert res.mimetype == utils.JSON_MIME_TYPE
        assert res.json == {'status': 'ok'}

    def test_not_found(self, accept_json, client):
        res = client.get('/', headers=accept_json)

        assert res.status_code == 404
        assert res.mimetype == utils.JSON_MIME_TYPE
        assert res.json == {'error': 'Not Found'}
