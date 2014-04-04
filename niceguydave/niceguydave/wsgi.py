"""
WSGI config for niceguydave project.
"""
import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niceguydave.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'StagingSettings')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
