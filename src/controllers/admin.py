from src.services.admin import Admin

def turn_into_admin(id) -> dict:
   try:
      admin = Admin()
      response = admin.turn_into_admin(id)
      return {'status': 'success', 'message': response}

   except Exception as err:
      return {'status': 'error', 'message': err}