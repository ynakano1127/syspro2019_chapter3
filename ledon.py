import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

for i in range(10):
    GPIO.output(14, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(14, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()

