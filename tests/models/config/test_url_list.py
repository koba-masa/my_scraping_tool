import pytest
import os

from models.config.url_list import UrlList

URL_LIST_TEST = 'config/test/urls/for_url_list.txt'

def test_init():
  assert type(UrlList(URL_LIST_TEST)) is UrlList

def test_init_without_params():
  with pytest.raises(TypeError):
    UrlList()

def test_init_not_exists_file():
  with pytest.raises(FileNotFoundError):
    UrlList("tests/test_not_exists_url_list.txt")

def test_read():
  results = UrlList(URL_LIST_TEST).read()
  assert type(results) is list
  assert "http://httpbin/status/301" in results
