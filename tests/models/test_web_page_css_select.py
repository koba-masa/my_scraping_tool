import pytest
import requests

from models.web_page import WebPage
from models.web_page_css_select import WebPageCssSelect

TARGET_URL = "http://localhost"
LOCATION = "http://localhost/location"

def test_create_instance():
  selector_name = "title"
  value = "タイトル"
  result = WebPageCssSelect(TARGET_URL, WebPage.UA_TYPE_PC, selector_name, value)
  assert type(result) is WebPageCssSelect
  assert result.url == TARGET_URL
  assert result.ua_type == WebPage.UA_TYPE_PC
  assert result.selector_name == selector_name
  assert result.value == value

def test_create_instance_with_wrong_params():
  with pytest.raises(Exception):
    WebPageCssSelect()
    WebPageCssSelect(TARGET_URL, WebPage.UA_TYPE_PC, "title")

def test_output():
  selector_name = "title"
  value = "タイトル"
  result = WebPageCssSelect(TARGET_URL, WebPage.UA_TYPE_PC, selector_name, value).output()
  assert result == TARGET_URL + "," + WebPage.UA_TYPE_PC + "," + selector_name + "," + value
