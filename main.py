import os

import webapp2

import basics


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Auto-debug mode if in localhost
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Development')

# Config vars that can be used calling in Handlers: self.app.config
CONFIG = {
}

# Routes
routes = basics.routes

# Start the WSGI app
app = webapp2.WSGIApplication(routes, debug=DEBUG, config=CONFIG)
