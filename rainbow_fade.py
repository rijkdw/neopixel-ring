import time
import board
import neopixel
import random
from color import Color


pixels = neopixel.NeoPixel(board.A0, 24, brightness=0.1, auto_write=False)
pixels.fill(Color(200, 50, 1).rgb)
pixels.show()

colors = Color.rainbow(n=1000)

t = 0
while True:
    t += 1
    for i in range(24):
        pixels[i] = colors[t%1000].rgb

    pixels.show()
    time.sleep(0.01)
