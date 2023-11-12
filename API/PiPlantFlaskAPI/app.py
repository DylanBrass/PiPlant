from RPi import GPIO
from flask import Flask
from flask_cors import cross_origin
from ligthFunctions.lightFunctionsFunctions import *
from moistureSensorFunc.moistureSensor import *

app = Flask(__name__)

LED1_PIN = 24
led1State = False

LED2_PIN = 23
led2State = False

allLights = {LED1_PIN: led1State, LED2_PIN: led2State}

GPIO.setmode(GPIO.BCM)

for pin in allLights.keys():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(LED1_PIN, allLights.get(pin))


@app.route('/numberOfLights')
@cross_origin()
def numberOfLightsEndpoint():
    return numberOfLights()


@app.route("/numberOfMoistureSensors")
@cross_origin()
def numberOfMoistureSensorsEndpoint():
    return numberOfMoistureSensors()


@app.route('/toggleLight/<lightNumber>', methods=['POST'])
@cross_origin()
def toggleLightEndpoint(lightNumber: int):
    return toggleLight(int(lightNumber))


@app.route('/getCurrentValues', methods=['GET'])
@cross_origin()
def getCurrentValueEndpoint():
    return getCurrentValueOfMoistureSensor()


@app.route("/getValuesForDay/<day>/<sensor_id>")
@cross_origin()
def getValuesForDayEndpoint(day, sensor_id):
    return getGraphData(day, sensor_id)


if __name__ == '__main__':
    app.run(threaded=True)

try:
    startCollectDataThread()
except KeyboardInterrupt:
    print('exiting script')
