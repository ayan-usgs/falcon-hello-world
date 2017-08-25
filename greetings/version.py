import falcon
import ujson

from . import app_logger, __version__


class AppVersion(object):

    log_msg = 'Request Type: {0}; URI: {1}.'

    def on_get(self, req, resp):
        app_logger.debug(self.log_msg.format(req.method, req.uri))
        version = __version__
        doc = {'applicationVersion': version}
        resp_body = ujson.dumps(doc, ensure_ascii=False)
        resp.body = resp_body
        resp.status = falcon.HTTP_200