import json
from src.color import Color


class Image:

    def __init__(self, colors: list[list[Color]]):
        self.colors = [[c.copy() for c in row] for row in colors]

    @classmethod
    def from_json_file(cls, filename: str):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
        colors = [[Color(*tuple(rgb)) for rgb in row] for row in data]
        return cls(colors)
    
    # ===========================================================
    # Methods

    def copy(self) -> 'Image':
        return Image(self.colors)

    def to_8bit(self):
        return Image([[c.to_8bit() for c in row] for row in self.colors])

    def show_on_pixels(self, neopixel, size=8, call_show=True):
        for y, row in enumerate(self.colors):
            for x, color in enumerate(row):
                neopixel[y*size + x] = color.rgb
        if call_show:
            neopixel.show()

    def transition_to(self, other: 'Image', spaces=0, include_first=True, include_last=True) -> list['Image']:
        images = []
        for i in range(0, 9+spaces):
            next_image_colors = [(row1 + [Color.black()]*spaces + row2)[i:i+8] for row1, row2 in zip(self.colors, other.colors)]
            next_image = Image(next_image_colors)
            images.append(next_image)
        if not include_first:
            images = images[1:]
        if not include_last:
            images = images[:-1]
        return images

    @staticmethod
    def transitions(images: list['Image']) -> list['Image']:
        frames = []
        for i in range(len(images)-1):
            frames += images[i].transition_to(images[i+1], include_last=i==len(images)-2)
        return frames