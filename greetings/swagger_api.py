import falcon
import ujson


class SwaggerAPI(object):

    definition = {'basePath': '/v2',
                     'host': 'petstore.swagger.io',
                     'info': {'contact': {'email': 'ayan@usgs.gov'},
                              'description': 'This is the api for a Python Falcon test application',
                              'license': {'name': 'Apache 2.0',
                                          'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'},
                              'termsOfService': 'http://swagger.io/terms/',
                              'title': 'Simple Hello World Application',
                              'version': '1.0.0'},
                     'paths': {'/hello_world': {'get': {'description': 'hello world get endpoint',
                                                        'parameters': [],
                                                        'responses': {'200': {'description': 'successful '
                                                                                             'return '
                                                                                             'value',
                                                                              'schema': {'additionalProperties': False,
                                                                                         'properties': {'message': {'type': 'string'}},
                                                                                         'type': 'object'}}}}},
                               '/version': {'get': {'description': 'application version number',
                                                    'parameters': [],
                                                    'responses': {'200': {'description': 'successful '
                                                                                         'return '
                                                                                         'value',
                                                                          'schema': {'additionalProperties': False,
                                                                                     'properties': {'applicationVersion': {'type': 'string'}},
                                                                                     'type': 'object'}}}}}},
                     'schemes': ['http'],
                     'swagger': '2.0'}

    def on_get(self, req, resp):
        resp_body = ujson.dumps(self.definition, ensure_ascii=False)
        resp.body = resp_body
        resp.status = falcon.HTTP_200
