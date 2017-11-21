import falcon

from .hello_world import HelloWorld
from .version import AppVersion
from .secrets import SecretText


api = application = falcon.API()

hi = HelloWorld()
av = AppVersion()
st = SecretText()

api.add_route('/hello_world', hi)
api.add_route('/version', av)
api.add_route('/secret', st)
