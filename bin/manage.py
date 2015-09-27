#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    sys.path.append('/home/ngspro/.www/')
    #sys.path.append('/home/cherry-girl/web/enggeo/ngspro/')
    sys.path.append('/home/ngspro/var/etc/')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
