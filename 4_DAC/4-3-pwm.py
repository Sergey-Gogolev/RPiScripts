import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    p = GPIO.PWM(23, 1000)

    while True:
        duty = float(input())
        print(3.3 * duty / 100, 'Volts')
        p.start(duty)

finally:
    print("Program was stopped by User")
    p.stop()
    GPIO.cleanup()