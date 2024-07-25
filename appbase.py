""" Aqui importamos apenas as partes do Django necessárias.
É recomendado não alterar o código deste módulo """

import sys
sys.dont_write_bytecode = True

import os
fpath = os.path.join(os.path.dirname(__file__), 'settings_db/')
sys.path.append(fpath)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from settings import env
import settings

from db.models import *
