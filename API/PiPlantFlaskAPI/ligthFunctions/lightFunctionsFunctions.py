import RPi.GPIO as GPIO
from flask import jsonify, abort
from app import allLights


def numberOfLights():
    return jsonify(numberOfLights=len(allLights))


def toggleLight(light: int):
    if light - 1 < len(allLights):
        lightPin = list(allLights.keys())[light - 1]
        allLights[lightPin] = not allLights.get(lightPin)
        GPIO.output(lightPin, allLights.get(lightPin))

        return jsonify(lightStatus=allLights[lightPin])

    abort(400)
