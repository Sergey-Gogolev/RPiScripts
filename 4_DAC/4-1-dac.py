import RPi.GPIO as GPIO

def decimal_to_binary(x):
        return [int(n) for n in bin(x)[2:].zfill(8)]


try:
        dac = [8, 11, 7, 1, 0, 5, 12, 6]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dac, GPIO.OUT)
        while True:
            i = int(round(float(input())))
            a = decimal_to_binary(i)
            print(round(3.3/256 * i, 3), '   Volts')
            GPIO.output(dac,a)


finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
    print("Program was stopped by User")