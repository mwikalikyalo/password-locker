from user import User

class Credentials:
  """ Documents the password details"""
  def __init__(self, page_name, username, password):
    self.page_name = page_name
    self.username = username
    self.password = password 
  
  password_list=[]

  def save_credentials(self):
    """ Save function for the new credentials"""
    Credentials.password_list.append(self)
  
  def delete_credentials(self):
    """ Delete function to delete unnecessary credentials"""
    Credentials.password_list.remove(self)

  @classmethod
  def credential_exists(cls, name):
        """Method to check whether a credential exists"""
        for credentials in cls.password_list:
            if credentials.username == name:
                return True
        return False

  def test_display_all_credentials(self):
      """TestCase to test whether all contacts can be displayed"""
      self.assertEqual(Credentials.display_credentials(), Credentials.password_list)
  

  
  

   


