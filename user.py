class User:
  """ Documents the user login initial details"""

  def __init__(self,full_name,username,email,password):
    self.full_name = full_name
    self.username = username
    self.email = email
    self.password = password

  user_details=[]  

  
  def save_user(self):
    """ Save function for the new user's details"""
    User.user_details.append(self) 

  def delete_account(self):
        """Delete function used to remove a selected account"""  
        User.user_details.remove(self) 
  
  @classmethod
  def find_by_user_name(cls, user_name):
    """Function checks whether the username provided by the username is available and if it is it returns the account"""
    for user in cls.user_details:
            if User.username == user_name:
                return user

  @classmethod
  def account_exists(cls, user_name):
        """This function loops through the present array of accounts while searching for the username entered by the user and returns true/false"""
        for account in cls.user_details:
            if User.username == user_name:
                return True
        return False

  @classmethod
  def display_accounts(cls):
      return cls.user_details
