import webapp2


class RequestObjectHandler(webapp2.RequestHandler):
    """
    This shows how to receive GET or POST requests. You can create other
    HTTP methods this way, such DELETE, HEAD, PUT etc
    """

    def get(self):
        params = self.request.arguments()

        self.response.content_type = 'text/html'
        self.response.out.write('This is a GET request!<br/>')
        if not params:
            return

        self.response.out.write('And you passed all these parameters:<br/>')
        for param_key in params:
            param_value = self.request.get(param_key)
            self.response.out.write('{}: {}<br/>'.format(param_key,
                                                         param_value))

