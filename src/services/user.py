#Imports
from src.models.user import create_user as create_user_models

class User:
   def __init__(self, userName, email, password) -> None:
      self.userName = userName
      self.email = email
      self.password = password
   
   def create_user(self):
      create_user_models(self.userName, self.email, self.password)