"""
WSGI config for niceguydave project.
"""
import os
import newrelic.agent
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

newrelic.agent.initialize('/var/www/niceguydave/newrelic.ini', 'live')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niceguydave.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'LiveSettings')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)
