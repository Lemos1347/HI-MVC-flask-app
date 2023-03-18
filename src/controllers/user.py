# Imports
from src.services.user import User
# import src.models.user as models


def create_user(user_name, email, password) -> dict:
    user = User(user_name=user_name, email=email, password=password)
    try:
        response = user.create_user()
        return {'type': 'success', 'message': f'{response}'}, 200
    except NameError as err:
        return {'type': 'error', 'message': f'{err}'}, 403
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}, 500


def login(email, password) -> dict:
    user = User(email=email, password=password)
    try:
        response, token = user.login()
        return {'type': 'success', 'message': f'{response}', 'token': f'{token}'}, 200
    except NameError as err:
        return {'type': 'error', 'message': f'{err}'}, 403
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}, 500

def get(id) -> dict:
    user = User()
    try:
        response = user.get(id)
        return {'type': 'success', 'content': response}, 200
    except NameError as err:
        return {'type': 'error', 'message': f'{err}'}, 403
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}, 500

def change_email(id, email) -> dict:
    user = User(email=email)
    try:
        response = user.change_email(id)
        return {'type': 'success', 'message': response}, 200
    except NameError as err:
        return {'type': 'error', 'message': f'{err}'}, 403
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}, 500

def delete_user(id) -> dict:
    user = User()
    try:
        response = user.delete_user(id)
        return {'type': 'success', 'message': response}, 200
    except NameError as err:
        return {'type': 'error', 'message': f'{err}'}, 403
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}, 500
