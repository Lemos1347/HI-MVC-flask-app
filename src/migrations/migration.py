import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
parent_parent_directory = os.path.dirname(parent_directory)
  
sys.path.append(parent_parent_directory)

from src import db, app, user, password
import pymysql
from user import User
from realty import Realty

conn = pymysql.connect(host='localhost', user=user, passwd=password, port=3306)
with conn.cursor() as cur:
    cur.execute('CREATE DATABASE IF NOT EXISTS ORMDB;')

with app.app_context():
   db.drop_all()
   db.create_all()
