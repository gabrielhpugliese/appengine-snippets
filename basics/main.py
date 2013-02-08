# Example of main.py

import webapp2

from home import views

# Every user that goes to '/' will make App Engine run Home view.
# But it will only enter here if specified in app.yaml
app = webapp2.WSGIApplication([('/', views.Home)], debug=True)
