from bs4 import BeautifulSoup
import requests

class Selector:
  def __init__(self, name, css_selector, att_key=None):
    self.name = name
    self.css_selector = css_selector
    self.att_key = att_key if att_key != '' else None
    self.is_text = True if self.att_key == None else False

  @classmethod
  def create(cls, selector_list):
    selectors = []
    for selector in selector_list:
      tmp = selector.split(',')
      selectors.append(Selector(tmp[0], tmp[1], tmp[2]))
    return selectors
      
class WebPage:
  UA_TYPE_PC = 'PC'
  UA_TYPE_SP = 'SP'
  USER_AGENT = {
    UA_TYPE_PC: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    UA_TYPE_SP: 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
  }

  def __init__(self, url, selectors):
    self.url = url
    self.selectors = selectors

  def get(self):
    results = []
    for selector in self.selectors:
      results.extend(self.select(selector, self.UA_TYPE_PC))
      results.extend(self.select(selector, self.UA_TYPE_SP))
    return results

  def select(self, selector, user_agent=UA_TYPE_PC):
    headers = {'user-agent': self.USER_AGENT[user_agent]}
    html = requests.get(self.url, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")
    elements = soup.select(selector.css_selector)
    results = None
    if selector.is_text:
      results = [self.url + ',' + user_agent + ',' + selector.name + ',' + e.get_text() for e in elements]
    else:
      results = [self.url + ',' + user_agent + ','+ selector.name + ',' + e[selector.att_key] for e in elements]
    return results

class File:
  def __init__(self, path):
    self.path = path

  def read(self):
    contents = []
    with open(self.path) as f:
      contents = [l.strip() for l in f.readlines()]
    return contents
  
  def write(self, contents):
    with open(self.path, mode='w') as f:
      f.write('\n'.join(contents))
    return

TARGET_URL_FILE = './url_list.txt'
TARGET_SELECTOR_FILE = './selector.csv'
RESULT_FILE = './result.csv'

def main():
  urls = File(TARGET_URL_FILE).read()
  selector_list = File(TARGET_SELECTOR_FILE).read()
  selectors = Selector.create(selector_list)
  results = []
  for url in urls:
    result = WebPage(url, selectors).get()
    results.extend(result)
  
  File(RESULT_FILE).write(results)

if __name__ == '__main__':
  main()
