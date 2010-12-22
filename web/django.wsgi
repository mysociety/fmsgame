#!/usr/bin/python 

import os, sys

file_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
path = os.path.normpath(file_dir + "/../fmsgame_project")
if path not in sys.path:
    sys.path.append(path)

# FIXME -- sort out duplicate paths in here FIXME (either: fmsgame_project or .., but not both)    
path = os.path.normpath(file_dir + "/../")
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
