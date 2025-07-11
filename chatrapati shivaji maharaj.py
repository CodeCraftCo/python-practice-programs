import turtle as t

t.bgcolor("orangered")
t.screensize(1400,1000)

corr = [(780,-209),(750,-208),(700,-207),(650,-206),
        (580,-205),(560,-203),(540,-200),(520,-198),
        (520,-193),(526,-190),(530,-180),(536,-172),
        (538,-160),(543,-123),(540,-112),(533,-100),
        (525,-86),(525,-80),(530,-60),(532,-40),
        (531,-24),(534,-21),(540,-23),(550,-26),
        (553,-30),(556,-40),(540,-90),(540,-108),
        (543,-120),(550,-126),(567,-136),(562,-120),
        (562,-115),(567,-100),(578,-80),(580,-76),
        (584,-60),(586,-40),(582,-20),(580,-14),
        (570,-9),(560,-5),(550,-6),(540,-8),
        (530,-11),(518,0),(512,8),(502,8),(500,10),
        (482,20),(470,36),(460,49),(468,63),(465,66),
        (470,80),(468,100),(466,110),(460,120),
        (458,123),(455,122),(452,130),(456,136),
        (460,145),(463,133),(459,128),(472,128),
        (468,140),(463,157),(470,157),(478,152),
        (475,166),(471,165),(460,162),(457,165),
        (443,165),(437,160),(427,153),(423,149),
        (424,138),(419,133),(419,130),(422,128),
        (423,127),(426,124),(423,120),(423,118),
        (420,116),(420,114),(428,116),(430,118),
        (432,118),(432,116),(428,114),(414,92),
        (405,84),(390,77),(386,79),(377,79),
        (375,76),(364,76),(357,88),(352,86),
        (348,92),(340,93),(330,96),(326,96),
        (320,92),(312,97),(307,92),(304,95),
        (306,100),(308,102),(307,104),(307,108),
        (304,107),(304,120),(303,124),(308,132),
        (300,129),(298,128),(288,120),(282,104),
        (283,100),(284,97),(288,92),(285,89),
        (278,87),(283,77),(281,72),(288,67),
        (287,59),(284,57),(284,54),(287,50),
        (286,48),(290,43),(288,40),(300,26),
        (298,17),(305,14),(312,15),(316,17),
        (320,20),(322,40),(324,47),(326,49),
        (333,40),(342,18),(343,3),(345,-6),
        (342,-18),(342,-22),(346,-36),(350,-38),
        (348,-43),(340,-41),(336,-37),(320,-33),
        (312,-40),(307,-47),(303,-100),(308,-115),
        (314,-118),(320,-120),(328,-122),(328,-110),
        (324,-103),(318,-100),(319,-61),(322,-57),
        (340,-60),(366,-78),(366,-100),(368,-106),
        (366,-120),(363,-140),(361,-157),(358,-163),
        (350,-166),(340,-178),(320,-164),(300,-151),
        (280,-140),(260,-130),(240,-122),(220,-112),
        (200,-102),(180,-100),(150,-98),(125,-96),
        (100,-94),(75,-92),(50,-90),(25,-88),
        (0,-86),(-25,-83),(-50,-81),(-75,-79),
        (-100,-77),(-125,-75),(-150,-72),(-175,-70),
        (-800,-68),
        (-800,-500),(800,-500),(800,-210)]

part1 = [(418,70),(412,73),(404,67),(393,64),
         (382,66),(382,60),(390,58),(392,50),
         (400,46),(402,48),(408,51),(417,58),(418,60)]

part2 = [(380,-186),(400,-190),(420,-193),(440,-195),
         (460,-197),(503,-199),(508,-186),(520,-174),
         (520,-162),(528,-158),(531,-127),(520,-113),
         (500,-106),(495,-102),(500,-117),(500,-123),
         (480,-132),(452,-153),(440,-153),(440,-163),
         (430,-177),(424,-180),(420,-176),(426,-160),
         (437,-144),(440,-145),(467,-122),(467,-120),
         (460,-107),(453,-100),(450,-85),(450,-72),
         (440,-74),(408,-72),(400,-80),(397,-80),
         (390,-77),(386,-85),(380,-108),(377,-123),
         (375,-140),(370,-160),(374,-166),(362,-180)]


name = [[(-560,320),(-560,300),(-590,300),(-590,220),(-560,220),
         (-560,200),(-610,200),(-610,320)],
        [(-530,320),(-530,270),(-510,270),(-510,320),(-490,320),
         (-490,200),(-510,200),(-510,250),(-530,250),(-530,200),
         (-550,200),(-550,320)],
        [(-460,320),(-460,270),(-440,270),(-440,320),(-420,320),
         (-420,200),(-440,200),(-440,250),(-460,250),(-460,200),
         (-480,200),(-480,320)],
        [(-350,320),(-350,200),(-370,200),(-370,250),(-390,250),
         (-390,200),(-410,200),(-410,320)],
        [(-280,320),(-280,300),(-300,300),(-300,200),(-320,200),
         (-320,300),(-340,300),(-340,320)],
        [(-210,320),(-210,250),(-230,250),(-210,200),(-230,200),
         (-250,250),(-250,200),(-270,200),(-270,320)],
        [(-140,320),(-140,200),(-160,200),(-160,250),(-180,250),
         (-180,200),(-200,200),(-200,320)],
        [(-70,320),(-70,250),(-110,250),(-110,200),
         (-130,200),(-130,320)],
        [(0,320),(0,200),(-20,200),(-20,250),(-40,250),
         (-40,200),(-60,200),(-60,320)],
        [(10,320),(70,320),(70,300),(50,300),(50,200),(30,200),
         (30,300),(10,300),(10,320)],
        [(80,320),(140,320),(140,300),(120,300),(120,220),(140,220),
         (140,200),(80,200),(80,220),(100,220),(100,300),(80,300),(80,320)]]


points = [[(-390,300),(-370,300),(-370,270),(-390,270),(-390,300)],
          [(-250,300),(-230,300),(-230,270),(-250,270),(-250,300)],
          [(-180,300),(-160,300),(-160,270),(-180,270),(-180,300)],
          [(-110,300),(-90,300),(-90,270),(-110,270),(-110,300)],
          [(-40,300),(-20,300),(-20,270),(-40,270),(-40,300)]]

def sun():
    t.penup()
    t.speed(5)
    t.goto(420,-220)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(240)
    t.end_fill()

def draw(c):
    t.penup()
    t.speed(7)
    t.goto(800,-210)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for i in range(len(c)):
        x, y = c[i]
        t.goto(x, y)
    t.end_fill()

def part(p,g):
    t.penup()
    t.speed(6)
    t.goto(g)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    for i in range(len(p)):
        x, y = p[i]
        t.goto(x, y)
    t.end_fill()

def names(n,p):
    #C
    t.penup()
    t.goto(-610,320)
    t.speed(5)
    t.pendown()
    t.color("#fdfae5")
    t.begin_fill()

    for i in range(len(n[0])):
        x, y = n[0][i]
        t.goto(x, y)
    t.end_fill()
    #H
    t.penup()
    t.goto(-550, 320)
    t.speed(5)
    t.pendown()
    t.color("#faf3c0")
    t.begin_fill()

    for i in range(len(n[1])):
        x, y = n[1][i]
        t.goto(x, y)
    t.end_fill()
    #H
    t.penup()
    t.goto(-480, 320)
    t.speed(5)
    t.pendown()
    t.color("#f5ea92")
    t.begin_fill()

    for i in range(len(n[2])):
        x, y = n[2][i]
        t.goto(x, y)
    t.end_fill()
    #A
    t.penup()
    t.goto(-410, 320)
    t.speed(5)
    t.pendown()
    t.color("#f3e260")
    t.begin_fill()

    for i in range(len(n[3])):
        x, y = n[3][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-390,300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[0])):
        x, y = p[0][i]
        t.goto(x, y)
    t.end_fill()


    #T
    t.penup()
    t.goto(-340, 320)
    t.speed(5)
    t.pendown()
    t.color("#f5dd29")
    t.begin_fill()

    for i in range(len(n[4])):
        x, y = n[4][i]
        t.goto(x, y)
    t.end_fill()

    #R
    t.penup()
    t.goto(-270, 320)
    t.speed(5)
    t.pendown()
    t.color("#f2d600")
    t.begin_fill()

    for i in range(len(n[5])):
        x, y = n[5][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-250, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[1])):
        x, y = p[1][i]
        t.goto(x, y)
    t.end_fill()

    #A
    t.penup()
    t.goto(-200, 320)
    t.speed(5)
    t.pendown()
    t.color("gold")
    t.begin_fill()

    for i in range(len(n[6])):
        x, y = n[6][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-180, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[2])):
        x, y = p[2][i]
        t.goto(x, y)
    t.end_fill()

    #P
    t.penup()
    t.goto(-130, 320)
    t.speed(5)
    t.pendown()
    t.color("#e6c60d")
    t.begin_fill()

    for i in range(len(n[7])):
        x, y = n[7][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-110, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[3])):
        x, y = p[3][i]
        t.goto(x, y)
    t.end_fill()

    #A
    t.penup()
    t.goto(-60, 320)
    t.speed(5)
    t.pendown()
    t.color("#d9b51c")
    t.begin_fill()

    for i in range(len(n[8])):
        x, y = n[8][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-40, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[4])):
        x, y = p[4][i]
        t.goto(x, y)
    t.end_fill()

    #T
    t.penup()
    t.goto(10, 320)
    t.speed(5)
    t.pendown()
    t.color("#cca42b")
    t.begin_fill()

    for i in range(len(n[9])):
        x, y = n[9][i]
        t.goto(x, y)
    t.end_fill()

    #I
    t.penup()
    t.goto(80, 320)
    t.speed(5)
    t.pendown()
    t.color("#bd903c")
    t.begin_fill()

    for i in range(len(n[10])):
        x, y = n[10][i]
        t.goto(x, y)
    t.end_fill()


part1Goto = (417,60)
part2Goto = (362,-180)

t.speed(15)
wn = t.Screen()
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
sun()
names(name,points)
draw(corr)
part(part1,part1Goto)

part(part2,part2Goto)

t.hideturtle()
t.Screen().exitonclick()
import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm

class sketch_from_svg:

    def __init__(self,path,scale=30,x_offset=350,y_offset=350):

        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale

    def hex_to_rgb(self,string):
        strlen = len(string)

        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2]*2
                g = string[2:3]*2
                b = string[3:4]*2
        elif strlen == 3:
                r = string[0:1]*2
                g = string[1:2]*2
                b = string[2:3]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]
        
        return int(r,16)/255,int(g,16)/255, int(b,16)/255

    def load_svg(self):
        print('Loading Data - Please Wait Few Seconds')
        paths,attributes,svg_att = svg2paths2(self.path)
        h = svg_att["height"]
        w = svg_att['width']
        self.height = int(h[:h.find('.')])
        self.width = int(w[:w.find('.')])

        res = []
        for i in tqdm(attributes):
            path = parse_path(i['d'])
            co = i['fill']
            col = self.hex_to_rgb(co)

            n = len(list(path))+2       
            pts = [((int((p.real/self.width)*self.scale))-self.x_offset, (int((p.imag/self.height)*self.scale))-self.y_offset) for p in (path.point(i/n) for i in range(0,n+1))]
            res.append((pts,col))
            tu.title("Made By CodeWithShani")

        print('SVG Data Loaded')
        return res

    def move_to(self,x, y):
        self.pen.up()
        self.pen.goto(x,y)
        self.pen.down()

    def draw(self,retain=True):
        coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)
        for path_col in coordinates:
            f = 1
            self.pen.color('black')

            path = path_col[0]
            col = path_col[1]

            self.pen.color(col)
            self.pen.begin_fill()

            for coord in path:
                x,y = coord
                y *= -1

                if f:
                    self.move_to(x, y)
                    f=0
                else:
                    self.pen.goto(x,y)
            self.pen.end_fill()
            writesomething()

        if retain == True:
            tu.done()

def writesomething():
    tu.goto(250,100)
    tu.write("CodeWithShani",font=("italian", "30", "bold"))
    tu.goto(210,50)
    tu.write("🙏 Jay Shree Ram 🙏",font=("italian", "30", "bold"))

pen= sketch_from_svg('2022_07_17.svg',scale=70)
pen.draw()
