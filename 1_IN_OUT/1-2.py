import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, 1)
time.sleep(3)
GPIO.output(19, 0)
time.sleep(3)
GPIO.output(19, 1)
