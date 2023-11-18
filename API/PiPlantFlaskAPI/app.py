import os

from flask import Flask, request
from flask_cors import cross_origin
from ligthFunctions.lightFunctionsFunctions import *
from moistureSensorFunc.moistureSensor import *
from Database.db_setup import *
from Database.db_fetch_functions import *
from Database.db_insert_functions import *

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY

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


@app.route("/getUsers")
@cross_origin()
def getUsersEndpoint():
    return fetchUsers()


@app.route("/createAccount", methods=['POST'])
@cross_origin()
def createAccountEndpoint():
    if request.method == 'POST':
        try:
            createUserDTO = request.get_json()
            return createUser(createUserDTO.get("username"), createUserDTO.get("password"))
        except Exception as e:
            print(e)

    abort(400)


@app.route("/login", methods=['POST'])
@cross_origin()
def loginEndpoint():
    try:
        loginDTO = request.get_json()
        return login(loginDTO.get("username"), loginDTO.get("password"))
    except Exception as e:
        print(e)


setUpDatabase()

if __name__ == '__main__':
    app.run(threaded=True)

try:
    startCollectDataThread()
except KeyboardInterrupt:
    print('exiting script')
