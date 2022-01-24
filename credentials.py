from user import User

class Credentials:
  """ Documents the password details"""
  def __init__(self, page_name, username, password):
    self.page_name = page_name
    self.username = username
    self.password = password 
  
  credentials=[]

  def __save_credentials(self):
    """ Save function for the new credentials"""
    Credentials.credentials.append(self)
  
  def __delete_credentials(self):
    """ Delete function to delete unnecessary credentials"""
    Credentials.credentials.remove(self)
