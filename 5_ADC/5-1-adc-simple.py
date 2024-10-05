import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
levels = 256
maxVolts = 3.3

def decimal_to_binary(x):
    return [int(n) for n in bin(x)[2:].zfill(8)]

def numer_to_dac(val):
    sig = decimal_to_binary(val)
    GPIO.output(dac, sig)
    return(sig)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:

        for val in range(256):
            sig = numer_to_dac(val)
            volts = val/ levels * maxVolts
            time.sleep(0.001)
            compVal = GPIO.input(comp)

            if compVal == 1:
                print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(val, sig, volts))
                break

except KeyboardInterrupt:
    print('Program was stopped by User')
else:
    print('No exceptions')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    print()
    print('VSE')
    print()