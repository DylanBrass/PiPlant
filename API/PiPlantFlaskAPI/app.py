from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route('/')
@cross_origin()
def hello_world():  # put application's code here
    """GET in server"""
    response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
    return response


if __name__ == '__main__':
    app.run()
