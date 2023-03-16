from flask import Blueprint, request, jsonify, g
import src.controllers.user as controller
from src.middleware.auth import auth

user = Blueprint('user', __name__)

@user.post('/create')
def handle_create():
    if request.is_json:
        try:
            data = request.json
            response = controller.create_user(user_name=data['user_name'], email=data['email'], password=data['password'])

            if response['type'] == 'error':
                response = {'message': f'{response["message"]}', 'code': 'ERROR'}
                return jsonify(response), 403
            
            response = {'message': f'{response["message"]}', 'code': 'SUCCESS'}
            return jsonify(response), 200

        except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return jsonify(response), 500

    else:
        response = {'message': 'Data not in json format', 'code': 'DENIED'}
        return jsonify(response), 404

@user.post('/login')
def handle_login():
    if request.is_json:
        try:
            data = request.json
            response = controller.login(email=data['email'], password=data['password'])
            response = {'token': f'{response}', 'code': 'SUCCESS'}
            return jsonify(response), 200

        except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return jsonify(response), 500

    else:
        response = {'message': 'Data not in json format', 'code': 'DENIED'}
        return jsonify(response), 404

@user.get('/')
@auth
def handle_get():
    id = g.get('id')
    try:
        response = controller.get(id)
        if response['type'] ==  'error':
            response = {'message': f'{response["message"]}', 'code': 'ERROR'}
            return jsonify(response), 403
        
        response = {'content': response['content'], 'code': 'SUCCESS'}
        return jsonify(response), 200
    
    except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return jsonify(response), 500

@user.put('/email')
@auth
def handle_change_email():
    if request.is_json:
        try:
            data = request.json
            id = g.get('id')
            response = controller.change_email(id=id, email=data['email'])

            if response['type'] == 'error':
                response = {'message': f'{response["message"]}', 'code': 'ERROR'}
                return jsonify(response), 403
            
            response = {'message': f'{response["message"]}', 'code': 'SUCCESS'}
            return jsonify(response), 200

        except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return jsonify(response), 500

    else:
        response = {'message': 'Data not in json format', 'code': 'DENIED'}
        return jsonify(response), 400

@user.delete('/delete')
@auth
def handle_delete_user():
    id = g.get('id')
    try:
        response = controller.delete_user(id)
        if response['type'] ==  'error':
            response = {'message': f'{response["message"]}', 'code': 'ERROR'}
            return jsonify(response), 403
        
        response = {'message': response['message'], 'code': 'SUCCESS'}
        return jsonify(response), 200
    
    except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return jsonify(response), 500