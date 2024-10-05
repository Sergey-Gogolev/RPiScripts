
import RPi.GPIO as G
import time
G.setmode(G.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
G.setup(leds, G.OUT)
j = 1
i = 0
while (j<4):
    for i in range(len(leds)):
        G.output(leds[i], 1)
        time.sleep(0.2)
        G.output(leds[i], 0)
    j = j + 1;

G.output(leds, 0)

G.cleanup()