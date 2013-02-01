from base_handler import BaseHandler


class Index(BaseHandler):
    def get(self):
        return self.render_response('basics/index.html')



