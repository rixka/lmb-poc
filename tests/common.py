import random

from flask import url_for
from pymongo import MongoClient


class MongoSystemTest(object):
    """ Base class for tests that use `~pymongo` """

    @classmethod
    def setup_class(cls):
        cls.db = MongoClient('localhost', 27017).development

        cls.cupcake_ids = list(cls.db.cupcakes.find({}, { '_id': 1 }).sort('_id'))

	cls.setup_class_custom()

    @classmethod
    def setup_class_custom(cls):
        pass

    @classmethod
    def seed_ratings(cls):
        for r in cls.cupcake_ids:
            object_id = r['_id']
            for i in range(0, random.randint(1, 10)):
                cls.db.ratings.insert({ 'cupcakeId': object_id, 'rating': random.randint(1, 5) })

        cls.rating_ids = list(cls.db.ratings.find({}, { '_id': 1 }).sort('_id'))


def build_query(api, items=None):
    items = items or []
    items.insert( 0, url_for(api) )
    return str.join('', items)

