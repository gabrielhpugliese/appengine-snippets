import os

import webapp2
from google.appengine.ext.webapp import template

from settings import PROJECT_ROOT_PATH
# PROJECT_ROOT_PATH is an automatic way to get the root path of the
# project. Check the code in settings.py in the project root.
TEMPLATES_ROOT_PATH = os.path.join(PROJECT_ROOT_PATH, 'templates')


class TemplateWithTagsHandler(webapp2.RequestHandler):
    """
    Same as the simple template example, except we are passing variables to
    template that we call template context.
    """

    def get(self):
        template_path = os.path.join(TEMPLATES_ROOT_PATH,
                                     'template_render/tags.html')
        template_context = {'templates_rock': 'Templates rock!',
                            'a_list': [x for x in xrange(5)]}
        self.response.out.write(template.render(template_path,
                                                template_context))
