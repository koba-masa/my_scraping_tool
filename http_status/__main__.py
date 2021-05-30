import requests

class WebPage:
  KEY_LOCATION = 'Location'
  def __init__(self, url, selectors=None):
    self.url = url
    self.selectors = selectors

  def get_status_code(self):
    response = requests.get(self.url, allow_redirects=False)
    location = response.headers[self.KEY_LOCATION] if self.KEY_LOCATION in response.headers else ''
    return [self.url + ',' + str(response.status_code) + ',' + location]

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
    result = WebPage(url).get_status_code()
    results.extend(result)
  File(RESULT_FILE).write(results)

if __name__ == '__main__':
  main()
