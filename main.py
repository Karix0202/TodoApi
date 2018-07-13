from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from database import config as db_config
from routes import config as routes_config
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the REST Api'})

if __name__ == '__main__':
    app.run(debug=True, host=routes_config.IP, port=3333)