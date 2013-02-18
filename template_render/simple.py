import webapp2
from google.appengine.ext.webapp import template


class SimpleTemplateHandler(webapp2.RequestHandler):
    """
    This shows the direct way to render a template with webapp2 and Django
    templates.
    """

    def get(self):
        """
        The template path above will be the project template path plus its
        subfolder template_render plus the template file simple.html
        """
        template_path = 'templates/template_render/simple.html'
        self.response.out.write(template.render(template_path, {}))





