import os

class Configuration(object):
    DEBUG = True
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
