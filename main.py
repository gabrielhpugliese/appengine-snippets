import webapp2

import basics
import settings


# Routes
routes = basics.routes

# Start the WSGI app
app = webapp2.WSGIApplication(routes, debug=settings.DEBUG)
