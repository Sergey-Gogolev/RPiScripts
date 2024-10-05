import RPi.GPIO as G

G.setmode(G.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
G.setup(leds, G.OUT)
G.setup(aux, G.IN)

while True:
    for i in range(len(leds)):
        G.output(leds[i], G.input(aux[i]))