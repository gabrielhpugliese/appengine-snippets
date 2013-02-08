import os

import webapp2
from google.appengine.ext.webapp import template

from settings import PROJECT_ROOT_PATH
# PROJECT_ROOT_PATH is an automatic way to get the root path of the
# project. Check the code in settings.py in the project root.
TEMPLATES_ROOT_PATH = os.path.join(PROJECT_ROOT_PATH, 'templates')


class SimpleTemplateHandler(webapp2.RequestHandler):
    """
    This shows the direct way to render a template with webapp2 and Django
    templates.
    """

    def get(self):
        template_path = os.path.join(TEMPLATES_ROOT_PATH,
                                     'template/simple.html')
        self.response.out.write(template.render(template_path, {}))





