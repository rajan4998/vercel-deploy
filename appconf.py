import mysql.connector
from flask import Flask,request
import psycopg2

class AppConfig:
    def __init__(self):
        # self.conn = mysql.connector.connect(
        #     host="ep-yellow-tree-a4zfakw4-pooler.us-east-1.aws.neon.tech",
        #     user="neondb_owner",         
        #     password="npg_pxHh86OMEAeB",  
        #     database="neondb"
        # )
        self.conn = psycopg2.connect("postgres://0197bb82-647f-7268-9bb8-b4202cee5de2:fd07b846-19a8-461d-928c-a7adfe72fe45@us-west-2.db.thenile.dev/nile_yellow_garden")
        self.app = None  # Placeholder for Flask app instance
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = '3o374eoxq0qiou4'  # Secret key for session management
        self.app.config['JWT_SECRET_KEY'] = '3o374eoxq0qiou4'  # Secret key for JWT
        self.app.config['JWT_TOKEN_LOCATION'] = ['headers']


