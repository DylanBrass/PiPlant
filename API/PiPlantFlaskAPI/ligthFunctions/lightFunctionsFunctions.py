import RPi.GPIO as GPIO
from flask import jsonify

LED1_PIN = 24
led1State = False

allLights = {LED1_PIN: led1State}

GPIO.setmode(GPIO.BCM)
for pin in allLights.keys():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(LED1_PIN, allLights.get(pin))


def toggleLight(light: int):
    global allLights
    lightPin = list(allLights)[light]
    allLights[lightPin] = not allLights.get(lightPin)
    GPIO.output(lightPin, allLights.get(lightPin))

    return jsonify(lightStatus=allLights[lightPin])
