import webapp2
from google.appengine.ext.webapp import template


class TemplateWithTagsHandler(webapp2.RequestHandler):
    """
    Same as the simple template example, except we are passing variables to
    template that we call template context.
    """

    def get(self):
        template_path = 'templates/template_render/tags.html'
        template_context = {'templates_rock': 'Templates rock!',
                            'a_list': [x for x in xrange(5)]}
        self.response.out.write(template.render(template_path,
                                                template_context))
