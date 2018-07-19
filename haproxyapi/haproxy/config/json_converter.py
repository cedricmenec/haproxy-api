import json
from haproxyapi.haproxy.config.serialization import HaProxyConfigSchema

class JsonConverter(object):
    """
    """
    def __init__(self):
        super(JsonConverter, self).__init__()

    def dump(self, config_obj, fp):
        """
        Serialize config_obj as a JSON formatted stream to fp (a .write()-supporting file-like object).
        This function use Python built-in json.dump() function and marshmallow library.

        Parameters
        ----------
        config_obj : pyhaproxy.config.Configuration
            HaProxy Configuration Object
        fp : file object
            a file-like object JSON stream will be persisted to.

        Returns
        -------
        str

        """
        return HaProxyConfigSchema().dump(config_obj)


    def dumps(self, config_obj):
        """
        Serialize HaProxy Configuration Object to JSON formatted string.

        Parameters
        ----------
        config_obj : pyhaproxy.config.Configuration
            HaProxy Configuration Object

        Returns
        -------
        str

        """
        return HaProxyConfigSchema().dumps(config_obj)
