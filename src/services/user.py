# Imports
import src.models.user as models
import jwt
from datetime import datetime, timedelta
import bcrypt

class User:
   def __init__(self,user_name:str="", email:str="", password:str="") -> None:
      self.user_name = user_name
      self.email = email
      self.password = password

   def create_user(self) -> str:
      try:
         models.already_exists_by_email(email=self.email)
      except:
         password = str(self.password)
         password = password.encode('UTF_8')
         password_crypt = bcrypt.hashpw(password, bcrypt.gensalt(10))

         models.create_user(self.user_name, self.email, password_crypt)

         return f"User {self.user_name} created with success!"
      
      raise NameError(f'User already exists with this email: {self.email}')
      

   def login(self) -> str:
      try:
         models.already_exists_by_email(email=self.email)
      except:
         raise NameError(f"User does not exists with the email: {self.email}")
      
      user = models.get_user_by_email(email=self.email)
      if bcrypt.checkpw(str(self.password).encode('UTF_8'), str(user.password).encode('UTF_8')):
         payload_data = {'id': user.id, "exp": datetime.utcnow() + timedelta(hours=2)}
         token = jwt.encode(payload=payload_data, key='secret')
         return "Login with success!", token
      
      raise NameError("Incorrect password!")

   def get(self, id) -> dict:
      user = models.get_user_by_id(id)
      return {'id': user.id, 'name': user.name, 'email': user.email}
   
   def change_email(self, id) -> str:
      return models.change_user_email(id, self.email)
   
   def delete_user(self, id) -> str:
      return models.delete_user_by_id(id)
