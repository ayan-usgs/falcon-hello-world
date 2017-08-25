# python-rest-api-reference


Simple API presenting a hello world endpoint implemented in Falcon.

All requirements specified in _requirements.txt_ must be installed
in your Python environment prior to running the application.

The application can be run by running: `gunicorn --reload greetings.app --config file:gunicorn_config.py`.

The application takes a single environment variable for configuration: `log_level`. Acceptable values for `log_level`
are: `DEBUG`, `INFO`, `WARNING`, `CRITICAL`, `ERROR`. If `log_level` is not provided, the application will default to
`INFO`.

The docker build requires that the version of the Python package be specified as well as the type. The type can either
be "releases" or "snapshots".