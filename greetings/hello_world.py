import datetime

import falcon
import ujson


class HelloWorld(object):

    def on_get(self, req, resp):
        utc_time = datetime.datetime.utcnow()
        utc_str = utc_time.strftime('%Y-%m-%d %H:%M:%S')
        doc = {'message': 'Hello World! The time is {} UTC.'.format(utc_str)}
        resp_body = ujson.dumps(doc, ensure_ascii=False)
        resp.body = resp_body
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        payload = req.stream.read()
        try:
            parsed = ujson.loads(payload)
        except ValueError:
            resp.status = falcon.HTTP_415
            resp.body = 'Only JSON content is supported.'
        else:
            keys = parsed.keys()
            doc = {'payloadKeys': keys}
            resp_body = ujson.dumps(doc, ensure_ascii=False)
            resp.status = falcon.HTTP_201
            resp.body = resp_body
