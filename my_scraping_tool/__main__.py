import sys

from services.http_status_getter import HttpStatusGetter


class MyScrapingTool:
  def execute(self, function_name):
    executor = None
    if function_name == 'http_status':
      executor = HttpStatusGetter('config/urls.txt')
    else:
      print("Specified function is not exist.: {function_name}")
      sys.exit(99)

    executor.execute()

if __name__ == '__main__':
  MyScrapingTool(sys.argv[0]).execute()
