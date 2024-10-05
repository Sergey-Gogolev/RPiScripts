import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(19, RPi.GPIO.OUT)
RPi.GPIO.output(19, 1)
