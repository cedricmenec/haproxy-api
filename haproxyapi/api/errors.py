import sys, traceback
from flask import Blueprint, jsonify
from haproxyapi.models.exceptions import HapiError

errors = Blueprint('error', __name__)

@errors.app_errorhandler(HapiError)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    return jsonify(response), status_code

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }
    # Print the traceback to the console
    traceback.print_tb(sys.exc_info()[2])
    return jsonify(response), status_code
