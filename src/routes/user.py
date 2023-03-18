from flask import Blueprint, request, jsonify, g
import src.controllers.user as controller
from src.middleware.auth import auth
from src.middleware.body_check import validate_body
from src.utils.body_schema.user import Schema

user = Blueprint('user', __name__)

@user.post('/create')
@validate_body(Schema.CREATE.value)
def handle_create():
    data = request.json
    response, code = controller.create_user(user_name=data['user_name'], email=data['email'], password=data['password'])
    return jsonify(response), code

@user.post('/login')
@validate_body(Schema.LOGIN.value)
def handle_login():
    data = request.json
    response, code = controller.login(email=data['email'], password=data['password'])
    return jsonify(response), code

@user.get('/')
@auth
def handle_get():
    id = g.get('id')
    response, code = controller.get(id)
    return jsonify(response), code

@user.put('/email')
@auth
@validate_body(Schema.PUT_EMAIL.value)
def handle_change_email():
    data = request.json
    id = g.get('id')
    response, code = controller.change_email(id=id, email=data['email'])
    return jsonify(response), code

@user.delete('/delete')
@auth
def handle_delete_user():
    id = g.get('id')
    response, code = controller.delete_user(id)
    return jsonify(response), code