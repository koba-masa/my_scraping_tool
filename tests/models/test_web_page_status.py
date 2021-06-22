import pytest
import requests

from models.web_page import WebPage
from models.web_page_status import WebPageStatus

TARGET_URL = "http://localhost"
LOCATION = "http://localhost/location"

def test_create_instance():
  assert type(WebPageStatus(TARGET_URL, WebPage.UA_TYPE_PC, requests.codes.ok, "")) \
    is WebPageStatus
  with pytest.raises(Exception):
    WebPageStatus()
    WebPageStatus(TARGET_URL, WebPage.UA_TYPE_PC, requests.codes.ok, LOCATION, "test")

def test_output():
  result = WebPageStatus(TARGET_URL, WebPage.UA_TYPE_PC, requests.codes.moved_permanently, LOCATION).output()
  assert result == TARGET_URL + "," + WebPage.UA_TYPE_PC + "," + str(requests.codes.moved_permanently) + "," + LOCATION
