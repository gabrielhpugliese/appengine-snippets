import webapp2
from webapp2_extras import jinja2


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
        return self.render_response('template/jinja2.html')

