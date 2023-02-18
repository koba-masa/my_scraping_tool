import pytest
import yaml

from models.config.settings import Settings

def test_config():
  assert Settings.config is None
  with open('config/test/settings.yml', 'r') as f:
      Settings.config = yaml.load(f, Loader=yaml.FullLoader)
  assert not Settings.config is None
