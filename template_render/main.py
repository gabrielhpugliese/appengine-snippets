import webapp2

config = {
    'webapp2_extras.jinja2': {
        'filters': {
            'pow2': lambda x: float(x) ** 2
        },
        'globals': {
            'upper': str.upper,
            'lower': str.lower
        },
        'template_path': ['templates']
    },
}

routes = [
    # Your routes
]

# Now we pass the config param to WSGIApplication
app = webapp2.WSGIApplication(routes, debug=True, config=config)
