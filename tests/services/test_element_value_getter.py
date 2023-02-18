import pytest

from services.element_value_getter import ElementValueGetter
from models.config.css_selector import CssSelector

URLS_CONFIG = 'config/test/urls/for_css_selector.txt'
CSS_SELECTORS_CONFIG = 'config/test/css_selectors/for_attribute_value.csv'

def test_init():
  instance = ElementValueGetter(URLS_CONFIG, CSS_SELECTORS_CONFIG)
  assert type(instance) is ElementValueGetter
  assert type(instance.urls) is list
  assert 'http://httpbin' in instance.urls
  assert type(instance.css_selectors) is list
  assert type(instance.css_selectors[0]) is CssSelector

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