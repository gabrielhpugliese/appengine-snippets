from base_handler import BaseHandler


class Index(BaseHandler):
    def get(self):
        return self.render_response('basics.html')


class HttpVerbsHandler(BaseHandler):

    def get(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def post(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def put(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def delete(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def options(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def head(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)

    def trace(self):
        self.response.content_type = 'text/plain'
        self.response.out.write(self.request)
