import os
import yaml

DEFAULT_CONFIG_FILENAME = "config.yml"

class HaProxyConfiguration(object):
    unix_socket = '/var/run/haproxy.sock'

    def __init__(self, config):
        if config.get("haproxy", {}).get("socket_file"):
            self.unix_socket = config["haproxy"]["socket_file"]


class ConfigurationLoader(object):

    def load(self, filename):
        """
        """
        with open(filename, 'r') as f:
            try:
                config = yaml.load(f)
            except yaml.YAMLError as exc:
                print(exc)
                return ""
        return config

class Configuration(object):
    """
    """
    DEBUG = True
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

    # Load configuration from YAML configuration file (config.yml)
    config_filename = os.path.join(APPLICATION_DIR, DEFAULT_CONFIG_FILENAME)
    config_loader = ConfigurationLoader()
    external_config = config_loader.load(config_filename)
    print(external_config)

    haproxy = HaProxyConfiguration(external_config)
