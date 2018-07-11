from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from database import SECRET_KEY, DB_URI

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

#Index
@app.route('/', methods = ['GET', 'POST'])
def index():
    return jsonify({'message': 'Welcome to the REST Api'})

#User
@app.route('/register', methods = ['POST'])
def register():
    request_json = request.get_json()

    return jsonify(request_json)

if __name__ == '__main__':
    app.run(debug=True)