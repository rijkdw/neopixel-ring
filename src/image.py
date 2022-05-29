import json
from src.color import Color


class Image:

    def __init__(self, pixels: list[list[Color]]):
        self.pixels = [[c.copy() for c in row] for row in pixels]

    @classmethod
    def from_json_file(cls, filename: str):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
        pixels = [[Color(*tuple(rgb)) for rgb in row] for row in data]
        return cls(pixels)
    
    # ===========================================================
    # Methods

    def to_8bit(self):
        return Image([[c.to_8bit() for c in row] for row in self.pixels])

    def show_on_pixels(self, neopixel):
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                neopixel[y*8 + x] = color.rgb
        neopixel.show()