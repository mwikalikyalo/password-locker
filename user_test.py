import unittest
from user import User

class TestUser(unittest.TestCase):
  def __setup__(self):
    self.new_user = User("Winnie Mwikali" , "mwiks" , "winnie@gmail.com" , "kyalo00'")
