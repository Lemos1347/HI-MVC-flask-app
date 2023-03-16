from flask import Blueprint, request, jsonify, g
import src.controllers.admin as controller
from src.middleware.auth import admin_auth

admin = Blueprint('admin', __name__)

@admin.put('/<int:id_to_change>')
@admin_auth
def handle_turn_into_admin(id_to_change):
   try:
      print(id_to_change)
      response = controller.turn_into_admin(id_to_change)

      if response['status'] == 'error':
         response = {'message': f'{response["message"]}', 'code': 'ERROR'}
         return jsonify(response), 403
      
      response = {'message': f'{response["message"]}', 'code': 'SUCCESS'}
      return jsonify(response), 200
   
   except Exception as err:
      response = {'message': err, 'code': 'ERROR'}
      return jsonify(response), 500