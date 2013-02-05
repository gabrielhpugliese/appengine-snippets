from webapp2_extras.routes import RedirectRoute, PathPrefixRoute

from views import Index
from simple import SimpleTemplateHandler
from tags import TemplateWithTagsHandler
from jinja2 import Jinja2TemplateHandler


routes = [
    RedirectRoute('/template/', Index, name='template_index',
                  strict_slash=True),
    PathPrefixRoute('/template', [
        RedirectRoute('/simple', SimpleTemplateHandler,
                      name='template_simple', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/with_tags', TemplateWithTagsHandler,
                      name='template_with_tags', methods=['GET'],
                      strict_slash=True),
        RedirectRoute('/jinja2', Jinja2TemplateHandler,
                      name='template_jinja2', methods=['GET'],
                      strict_slash=True),
    ])
]
