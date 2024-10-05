import RPi.GPIO as GPIO
import time

def decimal_to_binary(x):
        return [int(n) for n in bin(x)[2:].zfill(8)]


try:
        dac = [8, 11, 7, 1, 0, 5, 12, 6]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dac, GPIO.OUT)
        t = int(round(float(input())))
        while True:
            for a in range(256):
                GPIO.output(dac,decimal_to_binary(a))
                time.sleep(t/256)



finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
    print("Program was stopped by User")