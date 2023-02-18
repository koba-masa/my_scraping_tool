import pytest
import os
import glob

from services.base import Base
from services.element_value_getter import ElementValueGetter
from models.config.css_selector import CssSelector
from models.config.settings import Settings

URLS_CONFIG = 'config/test/urls/for_css_selector.txt'
CSS_SELECTORS_CONFIG = 'config/test/css_selectors/for_attribute_value.csv'
OUTPUT_FILE = 'tmp/test/*_element_value_getter.csv'

def test_init():
  instance = ElementValueGetter(URLS_CONFIG, CSS_SELECTORS_CONFIG)
  assert type(instance) is ElementValueGetter
  assert issubclass(ElementValueGetter, Base)
  assert type(instance.urls) is list
  assert 'http://httpbin' in instance.urls
  assert type(instance.css_selectors) is list
  assert type(instance.css_selectors[0]) is CssSelector
  assert not Settings.config['element_value_getter'] is None

def test_execute_with_attribute_value():
  instance = ElementValueGetter(URLS_CONFIG, CSS_SELECTORS_CONFIG)
  instance.execute()
  assert instance.results[0]['url'] == 'http://httpbin'
  assert instance.results[0]['selector_name'] == '_charset_'
  assert instance.results[0]['user_agent'] in ['PC', 'SP']
  assert instance.results[0]['value'] == 'UTF-8'

def test_execute_with_element_value():
  instance = ElementValueGetter(URLS_CONFIG, 'config/test/css_selectors/for_element_value.csv')
  instance.execute()
  assert instance.results[0]['url'] == 'http://httpbin'
  assert instance.results[0]['selector_name'] == 'title'
  assert instance.results[0]['user_agent'] in ['PC', 'SP']
  assert instance.results[0]['value'] == 'httpbin.org'

def test_execute_output_result():
  delete()
  assert len(glob.glob(OUTPUT_FILE)) == 0
  instance = ElementValueGetter(URLS_CONFIG, CSS_SELECTORS_CONFIG)
  instance.execute()
  assert not len(glob.glob(OUTPUT_FILE)) == 0
  delete()

def delete():
  for file in glob.glob(OUTPUT_FILE):
    os.remove(file)
