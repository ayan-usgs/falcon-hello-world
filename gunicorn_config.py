"""
Gunicorn configuration file.
"""
import os

import gunicorn


bind_ip = os.getenv('bind_ip', '0.0.0.0')
bind_port = os.getenv('bind_port', '7010')
bind = '{0}:{1}'.format(bind_ip, bind_port)
capture_output = True
ssl_keyfile = os.getenv('ssl_keyfile')
if ssl_keyfile is not None and os.path.isfile(ssl_keyfile):
    keyfile = ssl_keyfile
ssl_certfile = os.getenv('ssl_certfile')
if ssl_certfile is not None and os.path.isfile(ssl_certfile):
    certfile = os.getenv('ssl_certfile')
workers = 2
loglevel = os.getenv('log_level', 'info').lower()

gunicorn.SERVER_SOFTWARE = ''
