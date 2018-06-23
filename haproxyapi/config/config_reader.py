
class ConfigFileParser(object):
    """
    Used to read haproxy configuration file, and to return an HaproxyConfig object.
    """
    def __init__(self, filename):
        super(ConfigFileParser, self).__init__()
        self.filename = filename

    def parse():
        config = HaProxyConfig(self.filename)

        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        line_index = 0
        for i in range(line_index, len(lines)):
            if line.startswith('#')
                continue
            if line.startwith('backend')
                parse_result = parse_backend_block(lines, line_index)
                line_index = parse_result.get("line_index")
                config.add_backend(parse_result.get("backend"))

    def parse_backend_block(lines, index):
        

class HaProxyConfig(object):
    """docstring for HaProxyConfig."""
    def __init__(self, filename):
        super(HaProxyConfig, self).__init__()
        self.filename = filename
