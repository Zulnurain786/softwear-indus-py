"""
This script runs the Flask application using a development server.
"""

from os import environ
from app import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 5000
    app.run(host=HOST, port=PORT)
