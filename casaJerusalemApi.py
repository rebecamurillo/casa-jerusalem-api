import falcon
from src.routes.test import MyTest
from src.routes.user import User

# falcon.API instances are callable WSGI apps
app = falcon.API()

app.add_route('/test', MyTest())
app.add_route('/user', User())
