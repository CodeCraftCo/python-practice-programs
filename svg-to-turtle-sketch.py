import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm

class SketchFromSVG:
    def __init__(self, path, scale=30, x_offset=350, y_offset=350):
        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale  # fixed typo: was 'scalea'

    def hex_to_rgb(self, string):
        strlen = len(string)
        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1]*2
                g = string[2]*2
                b = string[3]*2
            else:
                # Handle unexpected length
                r, g, b = '00', '00', '00'
        elif strlen == 3:
            r = string[0]*2
            g = string[1]*2
            b = string[2]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16)/255, int(g, 16)/255, int(b, 16)/255

    def load_svg(self):
        print('Loading SVG data...')
        paths, attributes, svg_att = svg2paths2(self.path)
        h = svg_att["height"]
        w = svg_att["width"]
        self.height = int(float(h))
        self.width = int(float(w))

        res = []
        for attr in tqdm(attributes):
            path = parse_path(attr['d'])
            fill_color = attr.get('fill', '#000000')
            col = self.hex_to_rgb(fill_color)

            n = len(list(path)) + 2
            points = [(
                int((p.real / self.width) * self.scale) - self.x_offset,
                int((p.imag / self.height) * self.scale) - self.y_offset
            ) for p in (path.point(i / n) for i in range(n + 1))]
            res.append((points, col))
        print('SVG data loaded.')
        return res

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self, retain=True):
        coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        tu.colormode(1.0)  # Use RGB values from 0 to 1

        for points, col in coordinates:
            self.pen.color(col)
            self.pen.begin_fill()
            first = True
            for x, y in points:
                y = -y  # invert y-axis for turtle
                if first:
                    self.move_to(x, y)
                    first = False
                else:
                    self.pen.goto(x, y)
            self.pen.end_fill()

        if retain:
            tu.done()

# Example usage
pen = SketchFromSVG('hanumanji.svg', scale=70)
pen.draw()
