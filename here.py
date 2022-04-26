import time
import board
import neopixel
import random
from color import Color


pixels = neopixel.NeoPixel(board.A0, 24, brightness=0.3, auto_write=False)
pixels.fill(Color(200, 50, 1).rgb)
pixels.show()

colors = Color.gradientx([
    Color(255, 255, 0),
    Color(255, 0, 0),
    Color(0, 0, 255)
], n=24)

for i in range(24):
    pixels[i] = colors[i].rgb

pixels.show()
