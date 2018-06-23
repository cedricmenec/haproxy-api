import pytest
from config import ConfigurationLoader

def test_config_loader_file_not_found():
    loader = ConfigurationLoader()
    with pytest.raises(FileNotFoundError):
        loader.load("bad_file.yml")
