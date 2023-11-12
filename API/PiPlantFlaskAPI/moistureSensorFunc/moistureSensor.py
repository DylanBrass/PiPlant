import datetime
import time
import RPi.GPIO as GPIO
import pytz
from flask import jsonify, abort
import json
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
sensor1 = AnalogIn(ads, ADS.P0)

sensor2 = AnalogIn(ads, ADS.P1)

allMoistureSensors = [sensor1, sensor2]


def numberOfMoistureSensors():
    return jsonify(numberOfSensors=len(allMoistureSensors))


def percent_translation(raw_val, sensorNum: int):
    with open(f"cap_config_{sensorNum}.json") as json_data_file:
        config_data = json.load(json_data_file)
    per_val = abs((raw_val - config_data["zero_saturation"]) / (
            config_data["full_saturation"] - config_data["zero_saturation"])) * 100
    return round(per_val, 3)


def getCurrentValueOfMoistureSensor():
    allvalues = []

    counter = 1
    for sensor in allMoistureSensors:
        allvalues.append({"sensorNum": counter, "values": {"Value": percent_translation(sensor.value, counter), "Voltage": sensor.voltage}, "rawValue": sensor.value})
        counter += 1

    return jsonify(allValues=allvalues)


def getGraphData(date, sensorId):
    try:
        f = open(f"{date}-{sensorId}.csv", "r")
        s = f.readlines()
    except OSError:
        abort(404)

    combinedValues = []
    for value in s:
        value = value.split(",")
        combinedValues.append({"time": value[0], "value": value[1]})

    return jsonify(values=combinedValues)


def startCollectDataThread():
    threading.Thread(target=runCollectDataThread).start()


def runCollectDataThread():
    while True:
        collectDataSensor(60)


def collectDataSensor(WaitTime: int):
    try:
        tz = pytz.timezone('America/Montreal')
        local_time = datetime.datetime.now(tz)
        print(f"{local_time}")
        counter = 1
        for sensor in allMoistureSensors:

            fileName = f"{local_time.date()}-{counter}.csv"
            with open(fileName, "a") as f:
                f.write(f"{local_time.strftime('%I:%M %p')},{percent_translation(sensor.value, counter)},{sensor.voltage}\n")
            counter += 1

    except Exception as error:
        raise error
    except KeyboardInterrupt:
        print('exiting script')

    time.sleep(WaitTime)
