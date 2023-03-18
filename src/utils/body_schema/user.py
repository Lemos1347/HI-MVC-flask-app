from enum import Enum

class Schema(Enum):
     CREATE = {"type": "object", "properties": {"user_name": {"type": "string"}, "email": {"type": "string"}, "password": {"type": "string"}}, "required": ["user_name", "email", "password"]}

     LOGIN = {"type": "object", "properties": {"email": {"type": "string"}, "password": {"type": "string"}}, "required": ["email", "password"]}

     PUT_EMAIL = {"type": "object", "properties": {"email": {"type": "string"}}, "required": ["email"]}