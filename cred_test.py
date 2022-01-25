import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
  def __setup__(self):
    self.new_credentials = Credentials("Instagram","winnie","012345")
    
