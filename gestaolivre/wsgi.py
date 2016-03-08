# -*- coding: utf-8 -*-
u"""Configuração WSGI para o Gestão Livre."""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestaolivre.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

application = get_wsgi_application()
