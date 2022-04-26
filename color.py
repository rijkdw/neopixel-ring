class Color:

    # ==================================================================
    # Constructors

    def __init__(self, r, g, b):
        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))

        h, s, v = self.to_hsv()
        self.h = h
        self.s = s
        self.v = v

    def copy(self):
        return Color(self.r, self.g, self.b)

    @classmethod
    def from_hsv(cls, h, s, v):

        h %= 360
        c = s * v
        x = c * (1 - abs(h / 60 % 2 - 1))

        ra, ga, ba = 0, 0, 0
        if 0 <= h < 60:     ra, ga, ba = c, x, 0
        if 60 <= h < 120:   ra, ga, ba = x, c, 0
        if 120 <= h < 180:  ra, ga, ba = 0, c, x
        if 180 <= h < 240:  ra, ga, ba = 0, x, c
        if 240 <= h < 300:  ra, ga, ba = x, 0, c
        if 300 <= h < 360:  ra, ga, ba = c, 0, x

        m = v - c
        r, g, b = (ra + m) * 255, (ga + m) * 255, (ba + m) * 255
        return cls(r, g, b)

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls(r, g, b)

    @classmethod
    def from_hex(cls, hexcode):
        hexcode = hexcode.replace('#', '').strip()
        assert len(hexcode) == 6
        return cls(*tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4)))

    # ==================================================================
    # Methods

    def scaled(self, scalar):
        return Color(
            scalar * self.r,
            scalar * self.g,
            scalar * self.b
        )

    def to_rgb(self):
        return self.r, self.g, self.b

    @property
    def rgb(self):
        return self.to_rgb()

    def to_hsv(self):
        ra, ga, ba = self.r/255, self.g/255, self.b/255
        cmax = max(ra, ga, ba)
        cmin = min(ra, ga, ba)
        delta = cmax - cmin

        h = 0
        if delta == 0:    h = 0
        elif cmax == ra:  h = 60 * ((ga-ba)/delta % 6)
        elif cmax == ga:  h = 60 * ((ba-ra)/delta + 2)
        elif cmax == ba:  h = 60 * ((ra-ga)/delta + 4)

        s = 0
        if cmax == 0:  s = 0
        else:          s = delta/cmax

        v = cmax

        return h, s, v

    @property
    def hsv(self):
        return self.h, self.s, self.v

    def __str__(self):
        return f"{self.rgb}"

    def __repr__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b})"

    # ==================================================================
    # Static methods

    @staticmethod
    def color_list(r, g, b, length):
        return [Color(r, g, b) for _ in range(length)]

    @staticmethod
    def rainbow(n, s=1, v=1) -> List[Color]:
        hues = [360/n * i for i in range(n)]
        colors = [Color.from_hsv(h, s, v) for h in hues]
        return colors

    @staticmethod
    def gradient2(begin, end, n=1):
        print(f"gradient2({begin}, {end})")
        print(f"  hue change: {begin.h} --> {end.h}")
        if abs(end.h - begin.h) > 180:
            h_list = [begin.h+(begin.h-end.h)/n*(i+1) for i in range(n)]
        else:
            h_list = [begin.h+(end.h-begin.h)/n*(i+1) for i in range(n)]
        s_list = [begin.s+(end.s-begin.s)/n*(i+1) for i in range(n)]
        v_list = [begin.v+(end.v-begin.v)/n*(i+1) for i in range(n)]
        colors = [Color.from_hsv(h, s, v) for h, s, v in zip(h_list, s_list, v_list)]
        return colors

    @staticmethod
    def gradientx(colors, n=1, wraparound=False):
        if wraparound:
            colors += [colors[0].copy()]
        n -= 1
        div = len(colors)-1
        numbers = [n // div + (1 if x < n % div else 0) for x in range(div)]
        total_gradient = [colors[0]]
        for i in range(len(colors)-1):
            color0, color1 = colors[i], colors[i+1]
            subgradient = Color.gradient2(color0, color1, numbers[i])
            total_gradient += subgradient
        return total_gradient

    @staticmethod
    def sorted_by_hue(lst):
        return list(sorted(lst, key=lambda color: color.h))



