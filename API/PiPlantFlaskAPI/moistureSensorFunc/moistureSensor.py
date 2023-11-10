import datetime
import time
import RPi.GPIO as GPIO

from flask import jsonify, abort
import json
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading

# Create an ADS1115 ADC (16-bit) instance.

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
sensor1 = AnalogIn(ads, ADS.P0)

sensor2 = AnalogIn(ads, ADS.P1)

allMoistureSensors = [sensor1, sensor2]


def percent_translation(raw_val, sensorNum: int):
    with open(f"cap_config_{sensorNum}.json") as json_data_file:
        config_data = json.load(json_data_file)
    per_val = abs((raw_val - config_data["zero_saturation"]) / (
            config_data["full_saturation"] - config_data["zero_saturation"])) * 100
    return round(per_val, 3)


def getCurrentValueOfMoistureSensor():
    allvalues = []

    try:
        counter = 1
        for sensor in allMoistureSensors:
            allvalues.append({"sensorNum": counter, "values": {"Value": sensor.value, "Voltage": sensor.voltage}})
            counter += 1
    except Exception as error:
        raise error
        GPIO.cleanup()
    except KeyboardInterrupt:
        print('exiting script')
        GPIO.cleanup()

    return jsonify(allValues=allvalues)


def getGraphData(date, id):
    try:
        f = open(f"{date}-{id}.csv", "r")
        s = f.readlines()
    except OSError:
        abort(404)

    return jsonify(s)


def startCollectDataThread():
    try:
        threading.Thread(target=runCollectDataThread).start()
    except KeyboardInterrupt:
        print('exiting script')
        GPIO.cleanup()


def runCollectDataThread():
    while True:
        try:
            collectDataSensor(10)
        except KeyboardInterrupt:
            print('exiting script')
            GPIO.cleanup()


def collectDataSensor(WaitTime: int):
    try:
        counter = 1
        for sensor in allMoistureSensors:
            fileName = f"{datetime.date.today()}-{counter}.csv"
            counter += 1
            f = open(fileName, "a")
            f.write(f"{datetime.datetime.now().time().strftime('%I:%M %p')},{sensor.value},{sensor.voltage}\n")
    except Exception as error:
        raise error
        GPIO.cleanup()
    except KeyboardInterrupt:
        print('exiting script')
        GPIO.cleanup()

    time.sleep(WaitTime)
