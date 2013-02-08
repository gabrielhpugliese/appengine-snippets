import webapp2


class RequestObjectHandler(webapp2.RequestHandler):
    """
    This shows how to parse GET params, user_agent and referrer with
    self.request object
    """

    def get(self):
        params_html = ''
        params = self.request.arguments()
        user_agent = self.request.user_agent
        referrer = self.request.referrer
        self.response.content_type = 'text/html'

        html = '''This is a GET request!<br/><br/>
        <b>This is your user agent:</b><br/> {}<br/><br/>
        <b>This is the referrer:</b><br/> {}<br/><br/>'''.format(user_agent,
                                                                 referrer)
        if not params:
            return self.response.out.write(html)

        html = '{}{}<br/>'.format(
            html, '<b>And you passed all these parameters:</b>')

        for param_key in params:
            param_value = self.request.get(param_key)
            params_html = '{}<i>{}</i>: {}<br/>'.format(params_html, param_key,
                                                        param_value)

        html = '{}{}'.format(html, params_html)

        self.response.out.write(html)


