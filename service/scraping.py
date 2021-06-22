import requests
from bs4 import BeautifulSoup

from models.css_selector import CssSelector
from models.web_page import WebPage
from models.web_page_css_select import WebPageCssSelect

class Scraping:
  def select_by_css_selector(self, url, selectors):
    wp = WebPage(url)
    results = []
    # User-Agentごとにアクセス
    for ua in WebPage.USER_AGENT:
      response = wp.get(ua)
      soup = BeautifulSoup(response.content, "html.parser")
      # セレクタ数分ループ
      for selector in selectors:
        elements = soup.select(selector.css_selector)
        if selector.is_text:
          # 取得した要素数分ループ
          for element in elements:
            results.append(WebPageCssSelect(url, ua, selector.selector_name, element.get_text()))
        else:
          for element in elements:
            results.append(WebPageCssSelect(url, ua, selector.selector_name, element[selector.attribute_key]))
    return results
