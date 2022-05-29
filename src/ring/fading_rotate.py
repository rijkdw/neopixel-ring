import time
import board
import neopixel
import random
from color import Color
import math


pixels = neopixel.NeoPixel(board.A0, 24, brightness=0.1, auto_write=False)
pixels.fill(Color(255, 255, 255).rgb)
pixels.show()

colors = Color.rainbow(1000)

def f(theta):
    return max(0, 1 - theta/100)

angle = 0
i_color = 0
while True:
    for i in range(24):
        angle_i = i * 360 / 24
        theta = abs(angle - angle_i) % 360
        scalar = f(theta)
        pixels[i] = colors[i_color % 1000].scaled(scalar).rgb
    pixels.show()
    time.sleep(0.0001)
    angle += 10
    i_color += 1
