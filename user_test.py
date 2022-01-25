import unittest
from pip import main
from user import User

class TestUser(unittest.TestCase):
  def __setup__(self):
    self.new_user = User("Winnie Mwikali" , "mwiks" , "winnie7@gmail.com" , "kyalo00@")


  def test_init(self):
        """ Test to assert whether the values entered would appear when the roperty is called. """

        self.assertEqual(self.new_user.full_name, "Winnie Mwikali")
        self.assertEqual(self.new_user.username, "mwiks")
        self.assertEqual(self.new_user.email, "winnie7@gmail.com")
        self.assertEqual(self.new_user.password, "kyalo00@")


  def test_save_user(self):
        """Method that tests wether an user credentials have been successfully saved"""
        self.new_user.user_details()
        self.assertEqual(len(User.user_details), 1)

if __name__=="__main__":
    main()

  