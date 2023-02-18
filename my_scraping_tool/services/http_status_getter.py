import datetime

from services.base import Base
from models.config.url_list import UrlList
from models.web.page import Page
from models.web.user_agent import UserAgent
from models.result import Result
from models.config.settings import Settings

class HttpStatusGetter(Base):
  def __init__(self, urls_config):
    self.urls = UrlList(urls_config).read()
    self.results = []
    super().__init__()

  def execute(self):
    for url in self.urls:
      self.results.append(self.__get(url, UserAgent.pc(), 'PC'))
      self.results.append(self.__get(url, UserAgent.sp(), 'SP'))

    self.__output()

  def __get(self, url, user_agent, user_agent_name):
    page = Page(url, user_agent)
    result = {
      'url': url,
      'user_agent': user_agent_name,
      'status_code': str(page.http_status_code())
    }
    return result

  def __output(self):
    results = [','.join(result.values()) for result in self.results]
    timestamp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    file_name = self.__settings()['output']['file'].format(timestamp)
    Result.output(results, file_name)

  def __settings(self):
    return Settings.config['http_status_getter']
