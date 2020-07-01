import falcon
import json
from src.model.movie import Movie
from src.model.user import Users
from src.model.base import Base, Engine, Session
from datetime import date
import datetime
import logging



class User(object):

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

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        data = None

        print("hello world")
        if req.content_length:
            data = json.load(req.stream)      

        #TEST DB
        # 2 - generate database schema
        Base.metadata.create_all(Engine)

        # 3 - create a new session
        session = Session()

        # 4 - create movies
        todayDate = datetime.datetime.now
        print("todayDate")
        print(todayDate)
        user = Users(data["email"],data["name"],data["lastname"] )
        # 9 - persists data
        session.add(user)
        session.commit()
        session.close()

        resp.body = json.dumps(data)