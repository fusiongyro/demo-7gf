activate_this = '/srv/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from pyramid.paster import get_app, setup_logging
ini_path = '/srv/demo-7gf/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')