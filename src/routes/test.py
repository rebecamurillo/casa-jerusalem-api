import falcon
import json
from src.model.movie import Movie
from src.model.base import Base, Engine, Session
from datetime import date

class MyTest(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status

        #TEST DB
        # 2 - generate database schema
        Base.metadata.create_all(Engine)

        # 3 - create a new session
        session = Session()

        # 4 - create movies
        film1 = Movie("The Bourne Identity", date(2002, 10, 11))
        # 9 - persists data
        session.add(film1)


        data = { 'id': 1, 'name': 'Rebeca' }
        resp.body = json.dumps(data)

