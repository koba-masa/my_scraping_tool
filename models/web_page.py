import requests

from models.web_page_status import WebPageStatus

class WebPage:
  KEY_LOCATION = 'Location'
  UA_TYPE_PC = "PC"
  UA_TYPE_SP = "SP"
  USER_AGENT = {
    UA_TYPE_PC: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    UA_TYPE_SP: "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
  }

  def __init__(self, url):
    self.url = url

  def get(self, ua_type=UA_TYPE_PC, user_agent=None):
    ua = user_agent if not user_agent is None else self.USER_AGENT[ua_type]
    headers = {'user-agent': ua}
    response = requests.get(self.url, headers=headers)
    return response

  def get_status_code(self, user_agent={}):
    results = []
    ua = user_agent if user_agent else self.USER_AGENT
    for ua_type in ua:
        headers = {'user-agent': self.USER_AGENT[ua_type]}
        response = requests.get(self.url, headers=headers, allow_redirects=False)
        location = response.headers[self.KEY_LOCATION] if self.KEY_LOCATION in response.headers else ''

        results.append(WebPageStatus(self.url, ua_type, response.status_code, location))
    return results
