import time
import board
import neopixel
import random
from color import Color


fadeline = list(reversed([1, 0.8, 0.6, 0.4, 0.2, 0.1, 0.05, 0.02] + [0]*16))

pixels = neopixel.NeoPixel(board.A0, 24, brightness=0.5, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

colors = Color.rainbow(1000)
index = 0
while True:

    for i in range(24):
        pixels[i] = colors[index].scaled(fadeline[i]).rgb

    fadeline = [fadeline[-1]] + fadeline[:-1]

    index = (index + 1) % len(colors)

    pixels.show()
    time.sleep(0.1)

