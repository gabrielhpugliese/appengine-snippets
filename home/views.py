from boilerplate.lib.basehandler import BaseHandler


class Home(BaseHandler):
    def get(self):
        return self.render_template('home_index.html')
