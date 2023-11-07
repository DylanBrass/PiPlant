from flask import Flask
from flask_cors import cross_origin
import json
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import ligthFunctions.lightFunctionsFunctions
from moistureSensorFunc import moistureSensor
from ligthFunctions.lightFunctionsFunctions import *

app = Flask(__name__)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

with open("cap_config.json") as json_data_file:
    config_data = json.load(json_data_file)


# print(json.dumps(config_data))

def percent_translation(raw_val):
    per_val = abs((raw_val - config_data["zero_saturation"]) / (
            config_data["full_saturation"] - config_data["zero_saturation"])) * 100
    return round(per_val, 3)


@app.route('/getCurrentValue', methods=['GET'])
@cross_origin()
def toggleLight():
    ligthFunctions.lightFunctionsFunctions.toggleLight()


@app.route('/getCurrentValue', methods=['GET'])
@cross_origin()
def getCurrentValue():
    return moistureSensor.getCurrentValueOfMoistureSensor()


if __name__ == '__main__':
    app.run()
