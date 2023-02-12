from selenium import webdriver
import requests


class Page:
  def __init__(self, url, user_agent):
    self.url = url
    self.user_agent = user_agent
    self.status_code = None
    self.driver = None

  def get(self):
    self.__driver().get(self.url)
    self.__close()

    return self.http_status_code()

  def http_status_code(self, is_reget=False):
    if self.status_code is None or is_reget:
      headers = {'user-agent': self.user_agent}
      response = requests.get(self.url, headers=headers, allow_redirects=False)
      self.status_code = response.status_code
    return self.status_code

  def __driver(self):
    if self.driver is None:
      self.driver = webdriver.Remote(
        command_executor = 'http://selenium_server:4444/wd/hub',
        options=webdriver.ChromeOptions()
      )
    return self.driver

  def __close(self):
    self.driver.close()

