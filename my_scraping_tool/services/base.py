import os

class Base():
  def __init__(self):
    self.environment = os.getenv('ENV', 'production')

  def is_test(self):
    return self.environment == 'test'
