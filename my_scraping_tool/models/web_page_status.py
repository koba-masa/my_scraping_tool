class WebPageStatus:
  def __init__(self, url, ua_type, status_code, location):
    self.url = url
    self.ua_type = ua_type
    self.status_code = status_code
    self.location = location

  def output(self):
    return self.url + ',' + self.ua_type + ',' + str(self.status_code) + ',' + self.location
