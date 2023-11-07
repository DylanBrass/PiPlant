from flask import jsonify
import json
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

with open("cap_config.json") as json_data_file:
    config_data = json.load(json_data_file)
# Create an ADS1115 ADC (16-bit) instance.


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)


def percent_translation(raw_val):
    per_val = abs((raw_val - config_data["zero_saturation"]) / (
            config_data["full_saturation"] - config_data["zero_saturation"])) * 100
    return round(per_val, 3)


def getCurrentValueOfMoistureSensor():
    currentvalue = "Saturation : {:>5} : {:>5} Volts".format("Saturation", "Voltage\n")
    try:
        currentvalue = "SOIL SENSOR: " + "{:>5}%\t{:>5.3f}".format(percent_translation(chan.value), chan.voltage)
    except Exception as error:
        raise error
    except KeyboardInterrupt:
        print('exiting script')

    response = jsonify(currentValue=currentvalue)

    return response
