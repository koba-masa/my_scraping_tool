class WebPageCssSelect:
  def __init__(self, url, ua_type, selector_name, value):
    self.url = url
    self.ua_type = ua_type
    self.selector_name = selector_name
    self.value = value

  def output(self):
    return self.url + ',' + self.ua_type + ',' + self.selector_name + ',' + self.value
