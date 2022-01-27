import unittest

from pip import main
from credentials import Credentials

class TestUser(unittest.TestCase):
  def __setup__(self):
    """Set up method to run before each test cases."""
    self.new_credentials = Credentials("Instagram","winnie","012345")

  def test_init(self):
        """ Test to assert whether the values entered would appear when the property is called."""

        self.assertEqual(self.new_credentials.page_name, "Instagram")
        self.assertEqual(self.new_credentials.username, "winnie")
        self.assertEqual(self.new_credentials.password, "012345")

  def tearDown(self):
        """Method that clears the credentials_list after every test to ensure that there is no error"""
        Credentials.password_list = []
  

if __name__=="__main__":
    main()
    
