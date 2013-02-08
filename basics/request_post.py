import webapp2


class RequestPOSTObjectHandler(webapp2.RequestHandler):
    """
    This shows how to parse POST params and body
    """

    def post(self):
        params = self.request.arguments()
        body = self.request.body
        self.response.content_type = 'text/html'

        html = '''This is a POST request!<br/>
        It's inside a modal because you cannot do a href with POST.<br/>
        So, I'm doing an ajax with jQuery.<br/><br/>'''

        if params:
            params_html = ''

            for param_key in params:
                param_value = self.request.POST.get(param_key)
                params_html = '{}<i>{}</i>: {}<br/>'.format(params_html,
                                                            param_key,
                                                            param_value)

            html = '{}<b>And you passed all these parameters:</b><br/>{}'.format(
                html, params_html)

        if body:
            html = '{}<b>You can get the entire POST body:<br/></b>{}'.format(
                html, body)

        self.response.out.write(html)


