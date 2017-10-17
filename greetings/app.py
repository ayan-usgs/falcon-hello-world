import falcon
from falcon_swagger_ui import register_swaggerui_app

from .hello_world import HelloWorld
from .version import AppVersion
from .secrets import SecretText
from .swagger_api import SwaggerAPI


SWAGGER_URL = '/swagger'
API_URL = '/api'


api = application = falcon.API()

hi = HelloWorld()
av = AppVersion()
st = SecretText()
sa = SwaggerAPI()

api.add_route('/hello_world', hi)
api.add_route('/version', av)
api.add_route('/secret', st)
api.add_route(API_URL, sa)

register_swaggerui_app(application, SWAGGER_URL, API_URL)
