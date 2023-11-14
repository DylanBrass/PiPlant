from flask import Flask, request
from flask_cors import cross_origin
from ligthFunctions.lightFunctionsFunctions import *
from moistureSensorFunc.moistureSensor import *
from Database.db_setup import *
from Database.db_fetch_functions import *

app = Flask(__name__)


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


@app.route("/login", methods=['POST'])
@cross_origin()
def getUsersEndpoint():
    if request.method == 'POST':
        try:
            loginDTO = request.get_json()
            return login(loginDTO.get("username"), loginDTO.get("password"))
        except Exception as e:
            print(e)
            abort(400)

    abort(400)


setUpDatabase()

if __name__ == '__main__':
    app.run(threaded=True)

try:
    startCollectDataThread()
except KeyboardInterrupt:
    print('exiting script')
