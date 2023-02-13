from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


class Page:
  def __init__(self, url, user_agent):
    self.url = url
    self.user_agent = user_agent
    self.status_code = None
    self.driver = None
    self.contents = None

  def __del__(self):
    #print(self.driver)
    pass

  def get(self):
    self.__driver().get(self.url)
    self.contents = self.__driver().page_source
    self.__close()
    self.__quit()

    return self.http_status_code()

  def http_status_code(self, is_reget=False):
    if self.status_code is None or is_reget:
      headers = {'user-agent': self.user_agent}
      response = requests.get(self.url, headers=headers, allow_redirects=False)
      self.status_code = response.status_code
    return self.status_code

  def select_by_css_selector(self, css_selector):
    results = []
    if self.contents is None:
      raise AttributeError('Call get() method, before calling.')

    soup = BeautifulSoup(self.contents, "html.parser")
    elements = soup.select(css_selector)
    for element in elements:
      results.append(element)
    return results

  def __driver(self):
    if self.driver is None:
      self.driver = webdriver.Remote(
        command_executor = 'http://selenium_server:4444/wd/hub',
        options=webdriver.ChromeOptions()
      )
    return self.driver

  def __close(self):
    if not self.driver is None:
      self.driver.close()

  def __quit(self):
    if not self.driver is None:
      self.driver.quit()

