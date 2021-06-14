import requests

class WebPage:
  KEY_LOCATION = 'Location'
  UA_TYPE_PC = "PC"
  UA_TYPE_SP = "SP"
  USER_AGENT = {
    UA_TYPE_PC: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    UA_TYPE_SP: "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
  }

  def __init__(self, url, selectors=None):
    self.url = url
    self.selectors = selectors

  def get_status_code(self, user_agent=UA_TYPE_PC):
    headers = {'user-agent': self.USER_AGENT[user_agent]}
    response = requests.get(self.url, headers=headers, allow_redirects=False)
    location = response.headers[self.KEY_LOCATION] if self.KEY_LOCATION in response.headers else ''
    return [self.url + ',' + user_agent + ',' + str(response.status_code) + ',' + location]

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
    
TARGET_URL_FILE = 'url_list.txt'
RESULT_FILE = 'result.csv'

def main():
  urls = File(TARGET_URL_FILE).read()
  results = []
  for url in urls:
    result = WebPage(url).get_status_code(WebPage.UA_TYPE_PC)
    results.extend(result)
    result = WebPage(url).get_status_code(WebPage.UA_TYPE_SP)
    results.extend(result)
  File(RESULT_FILE).write(results)

if __name__ == '__main__':
  main()
