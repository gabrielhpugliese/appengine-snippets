from webapp2_extras.routes import RedirectRoute, PathPrefixRoute

import views


routes = [
    RedirectRoute('/basics/', views.Index, name='index', strict_slash=True),
    PathPrefixRoute('/basics', [
        RedirectRoute('/http_verbs/get', views.HttpVerbsHandler,
                      name='http_verbs_get', methods=['GET'],
                      strict_slash=True)
    ])
]
