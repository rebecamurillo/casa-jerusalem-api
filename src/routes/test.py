import falcon
import json


class MyTest(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status

        data = { 'id': 1, 'name': 'Rebeca' }
        resp.body = json.dumps(data)

