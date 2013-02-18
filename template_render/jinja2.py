import webapp2
from webapp2_extras import jinja2


class Jinja2TemplateHandler(webapp2.RequestHandler):
    """
    This is an advanced template with Jinja2.
    It passes global variables and filters to templates that can be used like
    it is Python code.

    Sources:
    - https://groups.google.com/forum/?fromgroups=#!topic/google-appengine-python/YNCUxuGzmwc
    """

    def render_response(self, template, template_context={}):
        # Renders a template and writes the result to the response.
        rv = jinja2.get_jinja2(app=self.app).render_template(template,
                                                             **template_context)
        return self.response.out.write(rv)

    def get(self):
        """
        If you make a new View/Handler, inherit it from a Handler like this one,
        so you will only need to do this once:
        """
        template_path = 'template_render/jinja2.html'
        return self.render_response(template_path)

