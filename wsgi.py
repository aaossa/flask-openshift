#!/usr/bin/env python
import os
from flask_openshift_template import app


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, app)
    httpd.serve_forever()
