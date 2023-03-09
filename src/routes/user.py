from flask import Blueprint, request, jsonify, make_response
from src.controllers.user import create_user

user = Blueprint('user', __name__)

@user.post('/create')
def handle_create():
    if request.is_json:
        try:
            data = request.json
            response = create_user(userName=data['userName'], email=data['email'], password=data['password'])
            response = {'message': f'{response}', 'code': 'SUCCESS'}
            return make_response(jsonify(response), 200)

        except Exception as err:
            response = {'message': f'{err}', 'code': 'ERROR'}
            return make_response(jsonify(response), 500)

    else:
        response = {'message': 'Data not in json format', 'code': 'DENIED'}
        return make_response(jsonify(response), 404)

# @user.post('/post')
# def handle_post():
#     return "Helllo Post!"