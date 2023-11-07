import RPi.GPIO as GPIO

LED1_PIN = 12
led1State = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.output(LED1_PIN, GPIO.LOW)

def toggleLight():
    print("Toggling Light !")
    GPIO.output(LED1_PIN, GPIO.HIGH)
