import datetime
import time

from flask import jsonify
import json
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading

with open("cap_config.json") as json_data_file:
    config_data = json.load(json_data_file)
# Create an ADS1115 ADC (16-bit) instance.


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
sensor1 = AnalogIn(ads, ADS.P0)

sensor2 = AnalogIn(ads, ADS.P1)

allMoistureSensors = [sensor1, sensor2]


def percent_translation(raw_val):
    per_val = abs((raw_val - config_data["zero_saturation"]) / (
            config_data["full_saturation"] - config_data["zero_saturation"])) * 100
    return round(per_val, 3)


def getCurrentValueOfMoistureSensor():
    allvalues = {}

    try:
        counter = 1
        for sensor in allMoistureSensors:
            allvalues[counter] = {"Value": sensor.value, "Voltage": sensor.voltage}
            counter += 1
    except Exception as error:
        raise error
    except KeyboardInterrupt:
        print('exiting script')

    return jsonify(allValues=allvalues)


def startCollectDataThread():
    threading.Thread(target=collectDataSensor()).start()


def collectDataSensor():

    while True:
        fileName = f"{datetime.date.today()}.txt"
        f = open(fileName, "a")
        f.write("Now the file has more content!")
        time.sleep(3)
