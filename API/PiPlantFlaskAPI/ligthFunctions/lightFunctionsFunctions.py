import RPi.GPIO as GPIO

LED1_PIN = 24
led1State = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.output(LED1_PIN, led1State)


def toggleLight():
    global led1State
    print("Toggling Light !")
    led1State = not led1State
    GPIO.output(LED1_PIN, led1State)
