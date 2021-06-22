import pytest
import requests

from models.web_page import WebPage
from models.web_page_status import WebPageStatus

def test_create_instane():
  assert type(WebPage("http://localhost")) is WebPage
  with pytest.raises(Exception):
    WebPage()
    WebPage("http://localhost", "test")

def test_can_get():
  assert type(WebPage("http://localhost/get").get() ) is requests.models.Response

def test_cannot_get_unexists_url():
  with pytest.raises(Exception):
    WebPage("https://localhost:433").get()

def test_get_status_code():
  target_url = "http://localhost"
  results = WebPage(target_url).get_status_code()
  assert type(results) is list
  assert type(results[0]) is WebPageStatus
  assert results[0].url == target_url
  assert results[0].ua_type == WebPage.UA_TYPE_PC or results[0].ua_type == WebPage.UA_TYPE_SP
  assert results[0].status_code == requests.codes.ok
  assert results[0].location == ""

def test_get_status_code_404_page():
  target_url = "http://localhost/status/404"
  results = WebPage(target_url).get_status_code()
  assert type(results) is list
  assert type(results[0]) is WebPageStatus
  assert results[0].url == target_url
  assert results[0].ua_type == WebPage.UA_TYPE_PC or results[0].ua_type == WebPage.UA_TYPE_SP
  assert results[0].status_code == requests.codes.not_found
  assert results[0].location == ""

def test_get_status_code_301_page():
  target_url = "http://localhost/status/301"
  results = WebPage(target_url).get_status_code()
  assert type(results) is list
  assert type(results[0]) is WebPageStatus
  assert results[0].url == target_url
  assert results[0].ua_type == WebPage.UA_TYPE_PC or results[0].ua_type == WebPage.UA_TYPE_SP
  assert results[0].status_code == requests.codes.moved_permanently
  assert results[0].location != ""
