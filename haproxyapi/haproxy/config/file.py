from pyhaproxy.parse import Parser
import pyhaproxy.config as config

class ConfigFileReader(object):
    def __init__(self):
        super(ConfigFileReader, self).__init__()

    def load(self, file_path):
        """
        Load and parse HaProxy Configuration file (haproxy.cfg)

        Parameters
        ----------
        file_path : str
            Full relative path to HaProxy configuration File (ex: /etc/haproxy/haproxy.cfg)

        Returns
        -------
        pyhaproxy.config.Configuration
            HaProxy Configuration Object

        """
        # Create an HaProxy Parser and parse the file
        parser = Parser(file_path)
        haproxy_config = parser.build_configuration()
        return haproxy_config
