import pytest
import requests

from models.web.page import Page

def test_init():
  url = 'http://httpbin'
  user_agent = 'user agent'
  instance = Page(url, user_agent)
  assert type(instance) is Page
  assert instance.url == url
  assert instance.user_agent == user_agent
  with pytest.raises(TypeError):
    Page()
    Page(url)
    Page(url, user_agent, 'test')

def test_get():
  url = 'http://httpbin'
  user_agent = 'user agent'
  instance = Page(url, user_agent)
  assert instance.get() == 200

def test_get_http_status_code():
  user_agent = 'user_agent'
  assert Page('http://httpbin/status/200', user_agent).http_status_code() == requests.codes.ok
  assert Page('http://httpbin/status/400', user_agent).http_status_code(True) == requests.codes.bad_request
  assert Page('http://httpbin/status/500', user_agent).http_status_code(False) == requests.codes.internal_server_error
