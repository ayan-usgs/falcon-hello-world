from hashlib import md5

import falcon
import ujson

from . import app_logger, secret_text


class SecretText(object):

    log_msg = 'Request Type: {0}; URI: {1}.'

    def on_get(self, req, resp):
        app_logger.debug(self.log_msg.format(req.method, req.uri))
        hash_result = md5(secret_text.encode('utf-8'))
        doc = {'secretTextHash': hash_result.hexdigest()}
        resp_body = ujson.dumps(doc, ensure_ascii=False)
        resp.body = resp_body
        resp.status = falcon.HTTP_200
