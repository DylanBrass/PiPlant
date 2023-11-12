import RPi.GPIO as GPIO
from flask import jsonify, abort

LED1_Ptick={{fontSize: 5, color: "#000000"}}IN = 24
led1State = False

LED2_PIN = 23
led2State = False

allLights = {LED1_PIN: led1State, LED2_PIN: led2State}

print("Starting lightFunctions")
GPIO.setmode(GPIO.BCM)

for pin in allLights.keys():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, allLights.get(pin))


def numberOfLights():
    return jsonify(numberOfLights=len(allLights))


def toggleLight(light: int):
    global allLights

    if light - 1 < len(allLights):
        lightPin = list(allLights.keys())[light - 1]
        allLights[lightPin] = not allLights.get(lightPin)
        GPIO.output(lightPin, allLights.get(lightPin))

        return jsonify(lightStatus=allLights[lightPin])

    abort(400)
