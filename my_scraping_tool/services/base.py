import os
import yaml

from models.config.settings import Settings

class Base():
  def __init__(self):
    self.environment = os.getenv('ENV', 'production')
    self.__read_settings()

  def is_test(self):
    return self.environment == 'test'

  def __read_settings(self):
    settings_path = self.__settings_path()
    if not os.path.exists(settings_path):
      raise FileNotFoundError()

    with open(settings_path, 'r') as f:
      Settings.config = yaml.load(f, Loader=yaml.FullLoader)

  def __settings_path(self):
    return 'config/settings.yml' if not self.is_test() else 'config/test/settings.yml'
