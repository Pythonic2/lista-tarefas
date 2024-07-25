#!/usr/bin/env python

import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'settings_db/')
sys.path.append(fpath)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
