import falcon
from src.routes.test import MyTest

# falcon.API instances are callable WSGI apps
app = falcon.API()

app.add_route('/test', MyTest())

