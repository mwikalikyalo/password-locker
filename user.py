from pip import main


class User:
  """ Documents the user login initial details"""

  def __init__(self,full_name,username,email,password):
    self.full_name = full_name
    self.username = username
    self.email = email
    self.password = password

  user_details=[]  

  
  def __save_user(self):
    """ Save function for the new user's details"""
    User.user_details.append(self) 


  def delete_account(self):
        """Delete function used to remove a selected account"""  
        User.user_details.remove(self) 
  

