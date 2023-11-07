from flask import Flask
from flask_cors import cross_origin
import time
import daemon
import ligthFunctions.lightFunctionsFunctions
import threading
from moistureSensorFunc import moistureSensor

app = Flask(__name__)


@app.route('/toggleLight', methods=['POST'])
@cross_origin()
def toggleLight():
    ligthFunctions.lightFunctionsFunctions.toggleLight()
    return '', 200


@app.route('/getCurrentValue', methods=['GET'])
@cross_origin()
def getCurrentValue():
    return moistureSensor.getCurrentValueOfMoistureSensor()


if __name__ == '__main__':
    app.run()
