#Imports
from src.services.user import User

def create_user(userName, email, password):
    user = User(userName, email, password)
    user.create_user()
    return 'User created with success!'
