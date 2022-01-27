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
  def test_find_credential_by_name(self):
        """Test to check if we can find credentials and display information"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "123333")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Twitter")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

  @classmethod
  def display_credentials(cls):
        """Method which displays all current credentials"""
        return cls.password_list

  @classmethod
  def credential_exists(cls, name):
        """Method to check whether a credential exists"""
        for credential in cls.password_list:
            if credential.user_name == name:
                return True
        return False
  
  
  

   


