

def preview(url, params=''):
    if params:
        params = '?{}'.format(params)
    html = '''
    <a href="{}{}" target="_blank">
        <button class="btn btn-success">
            Preview
        </button>
    </a>
    '''.format(url, params)
    return html


def docs(url, params=''):
    if params:
        params = '?{}'.format(params)
    html = '''
    <a href="{}{}" target="_blank">
        <button class="btn btn-info">
            Docs
        </button>
    </a>
    '''.format(url, params)
    return html
