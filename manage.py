#!/usr/bin/env python
import os
import sys

# load environment settings
try:
	from environment import environment
except:
	environment = ''

if __name__ == "__main__":
	if environment in ['development','testing','production']:
    	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneup.settings.%s' % environment)
    else:
    	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneup.settings')
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
