"""
This module shows many ways to render a template
"""
import os

import webapp2
from webapp2_extras import jinja2
from google.appengine.ext.webapp import template

from settings import PROJECT_ROOT_PATH
# PROJECT_ROOT_PATH is an automatic way to get the root path of the
# project. Check the code in settings.py in the project root.
# You can define a static path like /home/appengine/templates
TEMPLATES_ROOT_PATH = os.path.join(PROJECT_ROOT_PATH, 'templates')


class SimpleTemplateHandler(webapp2.RequestHandler):
    """
    This shows the direct way to render a template with webapp2 and Django
    templates.

    Source:
    - http://webapp-improved.appspot.com/tutorials/gettingstarted/templates.html
    """

    def get(self):
        template_path = os.path.join(TEMPLATES_ROOT_PATH,
                                     'basics/template/simple.html')
        self.response.out.write(template.render(template_path, {}))


class TemplateWithTagsHandler(webapp2.RequestHandler):
    """
    Same as the simple template example, except we are passing variables to
    template that we call template context.

    Source:
    - http://webapp-improved.appspot.com/tutorials/gettingstarted/templates.html
    """

    def get(self):
        template_path = os.path.join(TEMPLATES_ROOT_PATH,
                                     'basics/template/with_tags.html')
        template_context = {'templates_rock': 'Templates rock!',
                            'a_list': [x for x in xrange(5)]}
        self.response.out.write(template.render(template_path,
                                                template_context))


class Jinja2TemplateHandler(webapp2.RequestHandler):
    """
    This is an advanced template with Jinja2.
    It passes global variables and filters to templates that can be used like
    it is Python code.

    Sources:
    - http://stackoverflow.com/questions/7081250/webapp2-jinja2-how-can-i-get-uri-for-working-in-jinja2-views
    - http://jinja.pocoo.org/docs/api/
    """

    def jinja2_factory(self, app):
        j = jinja2.Jinja2(app)
        j.environment.filters.update({
            # Set filters.
            'pow2': lambda x: float(x) ** 2
        })
        j.environment.globals.update({
            # Set global variables.
            'upper': str.upper,
            'lower': str.lower
            # ...
        })
        return j

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(factory=self.jinja2_factory)

    def render_response(self, template, template_context={}):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(template, **template_context)
        return self.response.out.write(rv)

    def get(self):
        return self.render_response('basics/template/jinja2.html')

