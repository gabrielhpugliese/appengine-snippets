"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""

from webapp2_extras.routes import RedirectRoute

import basics
import template_render
from home.views import Home

ROUTES = ([RedirectRoute('/',  Home, name='home',
                         strict_slash=True)]
          + basics.routes
          + template_render.routes)


def add_routes(app):
    for route in ROUTES:
        app.router.add(route)
