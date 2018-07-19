import sys
import json
import datetime
from pprint import pprint

from flask import Blueprint, request, redirect, url_for, jsonify, make_response, abort

from haproxyapi import services

default = Blueprint('api',  __name__, template_folder='templates')


@default.route('/start', methods=['POST'])
def start():
    """
    Start haproxy service
    """
    result = services.start()
    if result["code"] == 0:
        return jsonify(result)
    else:
        return jsonify(result), 500


@default.route('/stop', methods=['POST'])
def stop():
    """
    Stop haproxy service
    """
    result = services.stop()
    if result["code"] == 3:
        return jsonify(result)
    else:
        return jsonify(result), 500


@default.route('/status', methods=['GET'])
def status():
    """
    Get status of haproxy service
    """
    result = services.status()
    return jsonify(result)

@default.route('/restart', methods=['POST'])
def restart():
    """
    Restart haproxy service
    """
    result = services.restart()
    if result["code"] == 0:
        return jsonify(result)
    else:
        return jsonify(result), 500

@default.route('/reload', methods=['POST'])
def reload():
    """
    Restart haproxy service
    """
    result = services.reload()
    if result["code"] == 0:
        return jsonify(result)
    else:
        return jsonify(result), 500


@default.route('/backends/<backend_name>/servers', methods=['GET'])
def list_servers(backend_name):
    """
    """
    results = services.list_servers(backend_name)
    return jsonify(results)


@default.route('/backends/<backend_name>/servers/<server_name>/disable', methods=['POST'])
def disable_server(backend_name, server_name):
    """
    """
    server = services.disable_server(backend_name, server_name)
    return jsonify(server)

@default.route('/backends/<backend_name>/servers/<server_name>/enable', methods=['POST'])
def enable_server(backend_name, server_name):
    """
    """
    server = services.enable_server(backend_name, server_name)
    return jsonify(server)


@default.route('/backends', methods=['GET'])
def list_backends():
    """

    """
    results = services.list_backends()
    return jsonify(results)
