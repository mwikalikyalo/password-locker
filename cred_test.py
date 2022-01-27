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

  def test_save_credentials(self):
        """Method that tests whether the new credential created has been saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.password_list), 1)

  def tearDown(self):
        """Method that clears the credentials_list after every test to ensure that there is no error"""
        Credentials.password_list = []

  def test_find_credential_by_name(self):
        """Test to check if we can find credentials and display information"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Facebook", "098765")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Facebook")
        self.assertEqual(found_credential.page_name, new_test_credential.page_name)

  def test_display_all_credentials(self):
    """TestCase to test whether all contacts can be displayed"""
    self.assertEqual(Credentials.display_credentials(), Credentials.password_list)
  
if __name__=="__main__":
    unittest.main()


    
if __name__=="__main__":
    main()
    
