from webapp2_extras.routes import RedirectRoute, PathPrefixRoute

from views import Index
from http_methods import HttpMethodsHandler
from template import (SimpleTemplateHandler, TemplateWithTagsHandler,
                      Jinja2TemplateHandler)


routes = [
    RedirectRoute('/basics/', Index, name='index', strict_slash=True),
    PathPrefixRoute('/basics', [
        RedirectRoute('/http_verbs/get', HttpMethodsHandler,
                      name='http_methods_get', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/http_verbs/post', HttpMethodsHandler,
                      name='http_methods_post', methods=['POST'],
                      strict_slash=True),
        RedirectRoute('/template/simple', SimpleTemplateHandler,
                      name='template_simple', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/template/with_tags', TemplateWithTagsHandler,
                      name='template_with_tags', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/template/jinja2', Jinja2TemplateHandler,
                      name='template_with_tags', methods=['GET'],
                      strict_slash=True),
    ])
]
