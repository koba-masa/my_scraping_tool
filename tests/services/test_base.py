import pytest
import os

from services.base import Base
from models.config.settings import Settings

def test_init_with_env():
  instance = Base()
  assert type(instance) is Base
  assert instance.environment == 'test'

def test_init_without_env():
  del os.environ['ENV']
  instance = Base()
  assert instance.environment == 'production'
  os.environ['ENV'] = 'test'

def test_init_read_settings():
  instance = Base()
  assert Settings.config['base']['sample'] == 'sample value'

def test_is_test():
  instance = Base()
  assert instance.is_test()
  del os.environ['ENV']
  instance = Base()
  assert not instance.is_test()
  os.environ['ENV'] = 'test'
