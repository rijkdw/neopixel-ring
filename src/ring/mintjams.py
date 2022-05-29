import time
import board
import neopixel
import random
from color import Color


pixels = neopixel.NeoPixel(board.A0, 24, brightness=0.1, auto_write=False)
pixels.fill(Color(15, 131, 103).rgb)
pixels.show()
