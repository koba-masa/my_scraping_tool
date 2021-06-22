from models.url_list import UrlList
from models.web_page import WebPage
from models.web_page_status import WebPageStatus
from models.result import Result

def main():
  urls = UrlList().read()
  results = []
  for url in urls:
    wp = WebPage(url)
    results.extend(wp.get_status_code())
  if not results:
    print("[WARN] 実行した結果何も取得できませんでした。")
    return
  result_csv = [result.output() for result in results]
  Result.output(result_csv)

if __name__ == '__main__':
  main()
