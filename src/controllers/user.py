# Imports
from src.services.user import User
# import src.models.user as models


def create_user(user_name, email, password) -> dict:
    user = User(user_name=user_name, email=email, password=password)
    try:
        response = user.create_user()
        return {'type': 'success', 'message': f'{response}'}
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}


def login(email, password) -> str:
    user = User(email=email, password=password)
    return user.login()

def get(id) -> dict:
    user = User()
    response_dict = user.get(id)
    return {'type': 'success', 'content': response_dict}

def change_email(id, email) -> dict:
    user = User(email=email)
    try:
        response = user.change_email(id)
        return {'type': 'success', 'message': f'{response}'}
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}

def delete_user(id) -> dict:
    user = User()
    try:
        response = user.delete_user(id)
        return {'type': 'success', 'message': response}
    except Exception as err:
        return {'type': 'error', 'message': f'{err}'}
