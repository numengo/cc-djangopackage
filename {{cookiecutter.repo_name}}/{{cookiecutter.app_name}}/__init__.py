__version__ = '{{ cookiecutter.version }}'

from simple_settings import LazySettings
settings = LazySettings('{{ cookiecutter.app_name }}.config.settings', '{{ cookiecutter.app_name|upper }}_.environ')

__all__ = [
    'settings',
]
