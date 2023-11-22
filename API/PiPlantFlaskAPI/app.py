import os
import uuid

from flask import Flask, request
from flask_cors import cross_origin, CORS
from ligthFunctions.lightFunctionsFunctions import *
from moistureSensorFunc.moistureSensor import *
from Database.db_setup import *
from Database.db_fetch_functions import *
from Database.db_insert_functions import *
from urllib.parse import urlparse
from SecurityFunctions.security import *

app = Flask(__name__)

CORS(app, supports_credentials=True)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'fairies-are-magic'
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/numberOfLights')
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def numberOfLightsEndpoint():
    return numberOfLights()


@app.route("/numberOfMoistureSensors")
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def numberOfMoistureSensorsEndpoint():
    return numberOfMoistureSensors()


@app.route('/toggleLight/<lightNumber>', methods=['POST'])
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def toggleLightEndpoint(lightNumber: int):
    return toggleLight(int(lightNumber))


@app.route('/getCurrentValues', methods=['GET'])
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def getCurrentValueEndpoint():
    print("Cookies" + str(request.cookies))
    return getCurrentValueOfMoistureSensor()


@app.route("/getValuesForDay/<day>/<sensor_id>")
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def getValuesForDayEndpoint(day, sensor_id):
    return getGraphData(day, sensor_id)


@app.route("/getUsers")
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def getUsersEndpoint():
    return fetchUsers()


@app.route("/register", methods=['POST'])
@cross_origin(allow_headers="*", supports_credentials=True)
def createAccountEndpoint():
    if request.method == 'POST':
        try:
            createUserDTO = request.get_json()
            return createUser(createUserDTO.get("username"), createUserDTO.get("password"))
        except Exception as e:
            print(e)

    abort(400)


@app.route("/login", methods=['POST'])
@cross_origin(allow_headers="*", supports_credentials=True)
def loginEndpoint():
    try:
        loginDTO = request.get_json()
        token = login(loginDTO.get("username"), loginDTO.get("password"))
        if token is None:
            abort(401)
        response = jsonify(username=loginDTO.get("username"), token=uuid.uuid4())
        domain = urlparse(request.base_url).hostname + ":3000"
        response.set_cookie("Bearer", token, httponly=True, max_age=900, path="/", samesite="None",
                            domain=domain, secure=False)
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        return response

    except Exception as e:
        print(e)
        abort(422)


@app.route("/logout", methods=['POST'])
@cross_origin(allow_headers="*", supports_credentials=True)
@secured_endpoint
def logoutEndpoint():
    response = jsonify()
    domain = urlparse(request.base_url).hostname + ":3000"
    response.set_cookie("Bearer", "", httponly=True, max_age=0, path="/", samesite="None", domain=domain)
    return response


setUpDatabase()

if __name__ == '__main__':
    app.run(threaded=True)

try:
    startCollectDataThread()
except KeyboardInterrupt:
    print('exiting script')
