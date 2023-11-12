from RPi import GPIO
from flask import Flask
from flask_cors import cross_origin
from ligthFunctions.lightFunctionsFunctions import *
from moistureSensorFunc import moistureSensor

GPIO.setwarnings(False)
GPIO.cleanup()


app = Flask(__name__)


@app.route('/numberOfLights')
@cross_origin()
def numberOfLights():
    return lightFunctionsFunctions.numberOfLights()


@app.route("/numberOfMoistureSensors")
@cross_origin()
def numberOfMoistureSensors():
    return moistureSensor.numberOfMoistureSensors()


@app.route('/toggleLight/<lightNumber>', methods=['POST'])
@cross_origin()
def toggleLight(lightNumber: int):
    return lightFunctionsFunctions.toggleLight(int(lightNumber))


@app.route('/getCurrentValues', methods=['GET'])
@cross_origin()
def getCurrentValue():
    return moistureSensor.getCurrentValueOfMoistureSensor()


@app.route("/getValuesForDay/<day>/<sensor_id>")
@cross_origin()
def getValuesForDay(day, sensor_id):
    return moistureSensor.getGraphData(day, sensor_id)


if __name__ == '__main__':
    app.run(threaded=True)

try:
    moistureSensor.startCollectDataThread()
except KeyboardInterrupt:
    print('exiting script')
