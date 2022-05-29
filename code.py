import time
import board
import neopixel
import json

from src.color import Color
from src.image import Image
from src.letter import Letter

# =================================================================================
# Set up the board

NUM_PIXELS = 64
PIN = board.A0

pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, brightness=0.03, auto_write=False)
pixels.fill(Color(0, 200, 0).rgb)
pixels.show()

print(len(pixels))

# =================================================================================
# Image load

# image1 = Image.from_json_file("assets/heart.json").to_8bit()
# image2 = Image.from_json_file("assets/dino.json").to_8bit()

# transition1 = image1.transition_to(image2, include_last=False)
# transition2 = image2.transition_to(image1, include_last=False, spaces=6)
# while True:
#     for image in transition1:
#         image.show_on_pixels(pixels)
#         time.sleep(0.1)
#     for image in transition2:
#         image.show_on_pixels(pixels)
#         time.sleep(0.1)

while True:
    for char in 'abcdefghijklmnopqrstuvwxyz':
    # for char in 'z':
        letter = Letter(char=char, color=(200, 50, 10))
        letter.show_on_pixels(pixels)
        time.sleep(0.5)