# -*- coding: utf-8
from django.apps import AppConfig
from . import settings

class {{ cookiecutter.app_config_name }}(AppConfig):
    name = '{{ cookiecutter.app_name }}'
