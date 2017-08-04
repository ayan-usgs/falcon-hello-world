import falcon

from .hello_world import HelloWorld
from .version import AppVersion


api = application = falcon.API()

hi = HelloWorld()
av = AppVersion()
api.add_route('/hello_world', hi)
api.add_route('/version', av)
