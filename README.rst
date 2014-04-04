===========
niceguydave
===========

This is the code for the niceguydave.com website.

To use this project follow these steps:

#. Create your working environment
#. Install additional dependencies
#. Test

*note: these instructions show the creation of a project called "niceguydave".
You should replace this name with the actual name of your project.*

Working Environment
===================

You have several options in setting up your working environment.  I recommend
using virtualenv to seperate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper
to help manage multiple virtualenvs across different projects.

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/dev.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Test the installation
=====================
running

    $ python manage.py test

will run the test suite.
