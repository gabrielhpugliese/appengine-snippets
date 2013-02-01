import webapp2


class HttpMethodsHandler(webapp2.RequestHandler):
    """
    This shows how to receive GET or POST requests. You can create other
    HTTP methods this way, such DELETE, HEAD, PUT etc
    """

    def get(self):
        self.response.content_type = 'text/plain'
        self.response.out.write('This is a GET request!')

    def post(self):
        self.response.content_type = 'text/plain'
        self.response.out.write('This is a POST request!')

