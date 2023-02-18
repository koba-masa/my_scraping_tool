import pytest
import os
import glob

from services.base import Base
from services.http_status_getter import HttpStatusGetter
from models.config.settings import Settings

URLS_CONFIG = 'config/test/urls/for_http_status.txt'
OUTPUT_FILE = 'tmp/result/test/*_http_status_getter.csv'

def test_init():
  instance = HttpStatusGetter(URLS_CONFIG)
  assert type(instance) is HttpStatusGetter
  assert issubclass(HttpStatusGetter, Base)
  assert type(instance.urls) is list
  assert 'http://httpbin/status/200' in instance.urls
  assert 'http://httpbin/status/400' in instance.urls
  assert 'http://httpbin/status/500' in instance.urls
  assert not Settings.config['http_status_getter'] is None

def test_execute():
  instance = HttpStatusGetter(URLS_CONFIG)
  instance.execute()
  assert 'url' in instance.results[0]
  assert 'user_agent' in instance.results[0]
  assert 'status_code' in instance.results[0]
  for result in instance.results:
    if result['url'] == 'http://httpbin/status/200':
      assert result['status_code'] == '200'
    elif result['url'] == 'http://httpbin/status/400':
      assert result['status_code'] == '400'
    elif result['url'] == 'http://httpbin/status/500':
      assert result['status_code'] == '500'

def test_execute_output_result():
  assert len(glob.glob(OUTPUT_FILE)) == 0
  instance = HttpStatusGetter(URLS_CONFIG)
  instance.execute()
  assert not len(glob.glob(OUTPUT_FILE)) == 0

def test_execute_output_result():
  delete()
  assert len(glob.glob(OUTPUT_FILE)) == 0
  instance = HttpStatusGetter(URLS_CONFIG)
  instance.execute()
  assert not len(glob.glob(OUTPUT_FILE)) == 0
  delete()

def delete():
  for file in glob.glob(OUTPUT_FILE):
    os.remove(file)
