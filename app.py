# Import Application configuration
from config import Configuration

import logging

# Import Flask and its ecosystem libs
from flask import Flask
from flask_cors import CORS

# Basic configuration of Python Logging sytem
logging.basicConfig()

# Create Flask application
app = Flask(__name__)

# Enable Cross Origin Request Sharing (CORS)
# on all "/api/" urls
CORS(app, resources={r"/api/*": {"origins": "*"}})

# TODO: What is this ?!
app.secret_key = 'some secret key'


# Configure application from a Configuration object
app.config.from_object(Configuration)
