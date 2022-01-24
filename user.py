from pip import main


class User:
  """ Documents the user login initial details"""
  user_details=[]

  def __init__(self,full_name,username,email,password):
    self.full_name = full_name
    self.username = username
    self.email = email
    self.password = password

  
  def __save_user(self):
    """ Save function for the new user's details"""
    User.__save_user.append(self)  
  
  del user_details(self)
  """ Delete function to delete user's details"""
  
  if __name__ == '__main__':
    main()

