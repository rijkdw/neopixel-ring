import time
import board
import neopixel
import json

from src.color import Color
from src.image import Image

# =================================================================================
# Set up the board

NUM_PIXELS = 64
PIN = board.A0

pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, brightness=0.03, auto_write=False)
pixels.fill(Color(0, 200, 0).rgb)
pixels.show()

# =================================================================================
# Image load

Image.from_json_file("assets/dino.json").show_on_pixels(pixels)

# =================================================================================
# Eye blinking