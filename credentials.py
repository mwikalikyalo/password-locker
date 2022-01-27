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
  def find_by_name(cls, page_name):
        """Method that takes in a name and returns a credential that matches that particular name"""
        for credentials in cls.password_list:
            if credentials.page_name == page_name:
                return credentials

  @classmethod
  def credential_exists(cls, name):
        """Method to check whether a credential exists"""
        for credentials in cls.password_list:
            if credentials.page_name == name:
                return True
        return False

  @classmethod
  def display_credentials(cls):
        """Method which displays all current credentials"""
        return cls.password_list

  
           
 
  

  
  

   


