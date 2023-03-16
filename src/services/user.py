# Imports
import src.models.user as models
import jwt
from datetime import datetime, timedelta


class User:
   def __init__(self,user_name:str="", email:str="", password:str="") -> None:
      self.user_name = user_name
      self.email = email
      self.password = password

   def create_user(self) -> str:
      models.create_user(self.user_name, self.email, self.password)
      return f"User {self.user_name} created with success!"

   def login(self) -> str:
      id = models.login(email=self.email, password=self.password)
      payload_data = {'id': id, "exp": datetime.utcnow() + timedelta(hours=2)}
      token = jwt.encode(payload=payload_data, key='secret')
      return token

   def get(self, id) -> dict:
      return models.get_user_by_id(id)
   
   def change_email(self, id) -> str:
      return models.change_user_email(id, self.email)
   
   def delete_user(self, id) -> str:
      return models.delete_user_by_id(id)
