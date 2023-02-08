import os

class UrlList:
  def __init__(self, url_list_path):
    if not os.path.exists(url_list_path):
      raise FileNotFoundError()
    self.url_list_path = url_list_path

  def read(self):
    urls = []
    with open(self.url_list_path) as f:
      urls = [l.strip() for l in f.readlines()]
    return urls
