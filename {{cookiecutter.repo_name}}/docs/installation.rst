============
Installation
============

At the command line::

    $ easy_install {{ cookiecutter.repo_name }}

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv {{ cookiecutter.repo_name }}
    $ pip install {{ cookiecutter.repo_name }}

Settings are managed using
`simple-settings <https://raw.githubusercontent.com/drgarcia1986/simple-settings>`__
and can be overriden with configuration files (cfg, yaml, json) or with environment variables
prefixed with {{ cookiecutter.repo_name|upper }}_.
