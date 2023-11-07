from flask import Flask
from flask_cors import cross_origin
import time
import daemon
import ligthFunctions.lightFunctionsFunctions
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
    return {'currentValue': "NAN"}
    # return moistureSensor.getCurrentValueOfMoistureSensor()


def fetchDataHourly():
    while True:
        time.sleep(3)
        print("Hello")


if __name__ == '__main__':
    app.run()

with daemon.DaemonContext():
    fetchDataHourly()
