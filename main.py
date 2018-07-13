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

app.config['SECRET_KEY'] = db_config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = db_config.DB_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()

    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'code': 1})

    hashed_pass = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], email=data['email'], password=hashed_pass, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'code': 2})

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the REST Api'})

if __name__ == '__main__':
    app.run(debug=True, host=routes_config.IP, port=3333)