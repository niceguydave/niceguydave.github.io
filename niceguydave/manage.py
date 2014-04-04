#!/usr/bin/env python
import os
import sys

#uncomment this line to use a local version of pan-libs
sys.path.insert(0, '/home/vagrant/dev/py/pan-libs')

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niceguydave.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'LiveSettings')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
