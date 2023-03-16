# Config to path of imports
import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
sys.path.append(parent_directory)

# Importing libraries
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

#Importing routes
from src.routes.user import user as user_routes
from src.routes.admin import admin as admin_routes

#MySQL database credentials
host = 'localhost:3306'
user = 'root'
password = 'rootpass12345'
database = 'ORMDB'
database_uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"

# App's config function
def create_app():
   app = Flask(__name__)
   # Enable cors
   CORS(app)

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   db = SQLAlchemy() 
   db.init_app(app)

   return app, db

app, db = create_app()
#Defining routes

app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(admin_routes, url_prefix='/admin')
# @app.before_first_request
# def create_tables():
#     db.create_all()

# Defining the routes
# app.route()
if __name__ == '__main__': 
   app.run(host='0.0.0.0', debug=True, port=3001)