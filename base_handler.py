import webapp2
from webapp2_extras import jinja2


def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.filters.update({
        # Set filters.
        # ...
    })
    j.environment.globals.update({
        # Set global variables.
        'uri_for': webapp2.uri_for,
        # ...
    })
    return j


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(factory=jinja2_factory)

    def render_response(self, template, template_context={}):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(template, **template_context)
        return self.response.out.write(rv)
