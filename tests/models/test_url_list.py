import pytest
import os

from models.url_list import UrlList

URL_LIST_TEST = 'tests/test_url_list.txt'

def before():
  with open(URL_LIST_TEST, mode='w') as f:
    f.write("http://localhost/status/200" + "\n")
    f.write("http://localhost/status/301" + "\n")

def after():
  os.remove(URL_LIST_TEST)

before()

def test_create_instance():
  assert type(UrlList()) is UrlList
  assert type(UrlList(URL_LIST_TEST)) is UrlList
  with pytest.raises(Exception):
    UrlList(URL_LIST_TEST, "test")
  with pytest.raises(FileNotFoundError):
    UrlList("tests/test_not_exists_url_list.txt")

def test_read():
  results = UrlList(URL_LIST_TEST).read()
  assert type(results) is list
  assert "http://localhost/status/301" in results

#after()