import falcon
import ujson

from . import app_logger, __version__


class AppVersion(object):

    def on_get(self, req, resp):
        app_logger.debug('{} request received.'.format(req.method))
        version = __version__
        doc = {'applicationVersion': version}
        resp_body = ujson.dumps(doc, ensure_ascii=False)
        resp.body = resp_body
        resp.status = falcon.HTTP_200