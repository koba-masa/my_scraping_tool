from models.url_list import UrlList
from models.web.page import Page
from models.web.user_agent import UserAgent

class HttpStatusGetter:
  def __init__(self, urls_config):
    self.urls = UrlList(urls_config).read()
    self.results = []

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
      'status_code': page.http_status_code()
    }
    return result

  def __output(self):
    # TODO: ファイル出力
    pass
