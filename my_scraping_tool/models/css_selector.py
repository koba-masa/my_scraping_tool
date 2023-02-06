import os

class CssSelector:
  DEFAULT_CSS_SELECTOR = 'config/css_selector.csv'
  CSV_COLMUN_COUNT = 3

  def __init__(self, selector_name, css_selector, attribute_key=None):
    self.selector_name = selector_name
    self.css_selector = css_selector
    self.attribute_key = attribute_key if attribute_key != '' else None
    self.is_text = True if self.attribute_key is None else False

  @classmethod
  def read(self, css_selector_path=DEFAULT_CSS_SELECTOR):
    if not os.path.exists(css_selector_path):
      raise FileNotFoundError()

    csv_lists = []
    with open(css_selector_path) as f:
      csv_lists = [l.strip() for l in f.readlines()]

    css_selectors = []
    for index, csv_line in enumerate(csv_lists):
      if csv_line == "":
        continue

      tmp = csv_line.split(',')
      if not len(tmp) == self.CSV_COLMUN_COUNT:
        raise Exception(str(index + 1) + "行目の項目数が間違っています。" + str(len(tmp)) + "/" + str(self.CSV_COLMUN_COUNT))
      css_selectors.append(CssSelector(tmp[0], tmp[1], tmp[2]))
    return css_selectors
