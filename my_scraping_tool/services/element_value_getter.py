from bs4 import BeautifulSoup
import datetime

from services.base import Base
from models.config.url_list import UrlList
from models.config.css_selector import CssSelector
from models.web.page import Page
from models.web.user_agent import UserAgent
from models.result import Result
from models.config.settings import Settings

class ElementValueGetter(Base):
  def __init__(self, urls_config, css_selectors_config):
    self.urls = UrlList(urls_config).read()
    self.css_selectors = CssSelector.read(css_selectors_config)
    self.results = []
    super().__init__()

  def execute(self):
    results = []
    for url in self.urls:
      results.extend(self.__get(url, UserAgent.pc(), 'PC', self.css_selectors))
      results.extend(self.__get(url, UserAgent.sp(), 'SP', self.css_selectors))
      # TODO: 並び順のソート
      self.results.extend(results)
    self.__output()

  def __get(self, url, user_agent, user_agent_name, css_selectors):
    page = Page(url, user_agent)
    page.get()
    results = []
    for css_selector in css_selectors:
      elements = page.select_by_css_selector(css_selector.css_selector)
      for element in elements:
        results.append(
          {
            'url': url,
            'selector_name': css_selector.selector_name,
            'user_agent': user_agent_name,
            'value': self.__value(element, css_selector)
          }
        )
    return results

  def __value(self, element, css_selector):
    return element.get_text() if css_selector.is_text else element[css_selector.attribute_key]

  def __output(self):
    results = [','.join(result.values()) for result in self.results]
    timestamp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    file_name = self.__settings()['output']['file'].format(timestamp)
    Result.output(results, file_name)

  def __settings(self):
    return Settings.config['element_value_getter']
