import time
import RPi.GPIO as G
G.setmode(G.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
G.setup(leds, G.OUT)
G.setup(24, G.IN)
int j = 0
int i = 0
while (j<4):
    for i in range[len(leds)]
        G.output(leds[i], 1)
        time.sleep(0.2)
        G.output(leds[i], 1)
    j++

 G.cleanup()