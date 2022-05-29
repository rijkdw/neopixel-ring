import time
import board
import neopixel
import json

from color import Color

# =================================================================================
# Set up the board

NUM_PIXELS = 64
PIN = board.A0

pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, brightness=0.1, auto_write=False)
# pixels.fill(Color(0, 100, 200).rgb)
# pixels.show()

# =================================================================================
# Image load

with open('assets/dino.json') as file:
    data = json.loads(file.read())

colors = [[Color(*tuple(rgb)).to_8bit() for rgb in row] for row in data]

for y, row in enumerate(colors):
    for x, color in enumerate(row):
        pixels[y*8 + x] = color.rgb
    print()
pixels.show()

# =================================================================================
# Eye blinking

eye_positions = [(1, 1), (3, 1)]


def close_eyes():
    skin_color = colors[0][1]
    for x, y in eye_positions:
        index = y*8 + x
        pixels[index] = skin_color.rgb
    pixels.show()

def open_eyes():
    for x, y in eye_positions:
        index = y*8 + x
        pixels[index] = (0, 0, 0)
    pixels.show()

while True:
    for i in range(3):
        close_eyes()
        time.sleep(0.2)
        open_eyes()
        time.sleep(0.6)
    time.sleep(2)