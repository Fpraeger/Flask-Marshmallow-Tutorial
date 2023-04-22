from flask import Flask, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

@app.route('/')
def hello_world():
        message = {'message': 'Hello, World!'}
        return jsonify(message)

if __name__ == '__main__':
    app.run()