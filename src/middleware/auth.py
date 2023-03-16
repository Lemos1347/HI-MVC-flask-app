import jwt
from flask import request, jsonify, g
from functools import wraps
from src.models import user as user_models


def auth(f):
   @wraps(f)
   def auth_function(*args, **kwargs):
      try:
         token = request.headers.get('authorization')
         decoded = jwt.decode(token, key='secret', algorithms=['HS256', ])
         g.id = decoded['id']
         return f(*args, **kwargs)
            
      except Exception as err:
         return jsonify({'type': 'error', 'message': f'{err}'}), 401
   return auth_function

def admin_auth(f):
   @wraps(f)
   def admin_auth_function(*args, **kwargs):
      try:
         token = request.headers.get('authorization')
         decoded = jwt.decode(token, key='secret', algorithms=['HS256', ])
         admin_status = user_models.get_admin_status_by_id(decoded['id'])
         if admin_status['is_admin'] == False:
            raise Exception('Not admin')
         g.id = decoded['id']
         return f(*args, **kwargs)
            
      except Exception as err:
         return jsonify({'type': 'error', 'message': f'{err}'}), 401
   return admin_auth_function
