from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from database import config
from werkzeug.security import generate_password_hash
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'message': 'Welcome to the REST Api'})

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

if __name__ == '__main__':
    app.run(debug=True)