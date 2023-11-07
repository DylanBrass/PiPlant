from flask import Flask
from flask_cors import cross_origin

import ligthFunctions.lightFunctionsFunctions
from moistureSensorFunc import moistureSensor

app = Flask(__name__)


@app.route('/toggleLight', methods=['POST'])
@cross_origin()
def toggleLight():
    print("Calling Toggling Light !")
    ligthFunctions.lightFunctionsFunctions.toggleLight()
    print("After Toggling light !")
    return '', 200


@app.route('/getCurrentValue', methods=['GET'])
@cross_origin()
def getCurrentValue():
    return {'currentValue': "NAN"}
    # return moistureSensor.getCurrentValueOfMoistureSensor()


if __name__ == '__main__':
    app.run()
