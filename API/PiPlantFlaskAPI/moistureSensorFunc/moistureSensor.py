from flask import jsonify

from app import percent_translation, chan


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
