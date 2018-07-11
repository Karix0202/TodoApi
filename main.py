from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'message': 'Welcome to the REST Api'})

if __name__ == '__main__':
    app.run(debug=True)