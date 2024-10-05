import RPi.GPIO as G
import time
G.setmode(G.BCM)
leds = [8, 11, 7, 1, 0, 5, 12, 6]
G.setup(leds, G.OUT)
number = [0, 0, 0, 0, 0, 0, 0, 0]
G.output(leds, number)
time.sleep(15)
G.output(leds, 0)

G.cleanup()