import sys

from services.http_status_getter import HttpStatusGetter
from services.element_value_getter import ElementValueGetter

class MyScrapingTool:
  URLS_CONFIG = 'config/urls.txt'
  CSS_SELECTORS_CONFIG = 'config/css_selector.csv'

  def execute(self, function_name):
    executor = None
    if function_name == 'http_status':
      executor = HttpStatusGetter(self.URLS_CONFIG)
    elif function_name == 'element_value':
      executor = ElementValueGetter(self.URLS_CONFIG, self.CSS_SELECTORS_CONFIG)
    else:
      print("Specified function is not exist.: {function_name}")
      sys.exit(99)

    executor.execute()

if __name__ == '__main__':
  MyScrapingTool(sys.argv[0]).execute()
