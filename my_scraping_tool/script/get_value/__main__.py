from models.url_list import UrlList
from models.config.css_selector import CssSelector
from models.web_page_css_select import WebPageCssSelect
from models.result import Result
from services.scraping import Scraping

def main():
  urls = UrlList().read()
  css_selectors = CssSelector.read()
  scraping = Scraping()
  results = []
  for url in urls:
    results.extend(scraping.select_by_css_selector(url, css_selectors))
  if not results:
    print("[WARN] 実行した結果何も取得できませんでした。")
    return
  result_csv = [result.output() for result in results]
  Result.output(result_csv)

if __name__ == '__main__':
  main()
