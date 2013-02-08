from webapp2_extras.routes import RedirectRoute, PathPrefixRoute

from views import Index
from http_methods import HttpMethodsHandler
from request_get import RequestGETObjectHandler
from request_post import RequestPOSTObjectHandler


routes = [
    RedirectRoute('/basics/', Index, name='basics_index', strict_slash=True),
    PathPrefixRoute('/basics', [
        RedirectRoute('/http_methods/get', HttpMethodsHandler,
                      name='http_methods_get', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/http_methods/post', HttpMethodsHandler,
                      name='http_methods_post', methods=['POST'],
                      strict_slash=True),
        RedirectRoute('/request/get', RequestGETObjectHandler,
                      name='request_get', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/request/post', RequestPOSTObjectHandler,
                      name='request_post', methods=['POST'],
                      strict_slash=True),
    ])
]
