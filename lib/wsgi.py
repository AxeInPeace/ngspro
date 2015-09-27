"""
WSGI config for ngspro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/ngspro/.www/')
#sys.path.append('/home/cherry-girl/web/enggep/ngspro/')
sys.path.append('/home/ngspro/var/etc/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
