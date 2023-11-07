import RPi.GPIO as GPIO

LED1_PIN = 12
led1State = False

GPIO.setmode(GPIO.BCM)

GPIO.output(LED1_PIN, led1State)


def toggleLight():
    led1State = True
    GPIO.output(LED1_PIN, led1State)
