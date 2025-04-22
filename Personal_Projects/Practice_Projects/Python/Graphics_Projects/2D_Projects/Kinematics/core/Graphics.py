import pygame as pg
import math



PI = math.pi

def angleInRad(radAngle):
    return radAngle*(PI/180)

def radToAngle(radVal):
    return radVal*(180/PI)

def sin(angle):
    return math.sin(angleInRad(angle))

def cos(angle):
    return math.cos(angleInRad(angle))

def tan(angle):
    if (angle != 90):
        return math.tan(angleInRad(angle))
    else:
        print("Ei! Tan of 90 is not defined!")

def atan(value):
    return radToAngle(math.atan(value))

def asin(value):
    return radToAngle(math.asin(value))

def acos(value):
    return radToAngle(math.acos(value))


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y


def drawLine(surface, color, startpos, endpos, width):
    """
        For future me, by th grace of God:
        This code is to gnerate an anti-aliased thick line. The thickness depends on the width.
        The function draws the line, based on the orientation of the main line formed by p1 and p2...
        it uses some trigonometry to find the angle of the line of p1 and p2 relative to the x-axis...
        then uses this angle to calculate the points of lines parallel to line p1-p2.
        The for loop iterates to draw these lines based on the width, calculating the corresponding points...
        for every width and then calling the aaline draw function
    """
    ##  Because startpos and endpos are tuples, index 0 and 1 are x and y respectively
    p1, p2 = Vector(startpos[0], startpos[1]), Vector(endpos[0], endpos[1])
    length = math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2)

    ##  This is the angle relative to the x-axis
    if (p2.x - p1.x) != 0:
        angle = atan((p2.y - p1.y) / (p2.x - p1.x))
    else:
        angle = 90
        # angle = asin((p2.y - p1.y) / length)

    ##  p3 is perpendicular to p1 and p4 is perpendicular to p2
    for i in range(width):
        for j in range(width):
            dx = ((width * 0.5) - i) * sin(angle)
            dy = ((width * 0.5) - i) * cos(angle)
            p3 = Vector(p2.x + dx, p2.y - dy)
            p4 = Vector(p1.x + dx, p1.y - dy)
            pg.draw.aaline(surface, color, (p3.x, p3.y), (p4.x, p4.y), 2)


def drawLineB(surface, color, startpos, endpos, width):

    ##  Because startpos and endpos are tuples, index 0 and 1 are x and y respectively
    p1, p2 = Vector(startpos[0], startpos[1]), Vector(endpos[0], endpos[1])

    length = math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2)

    ##  This is the angle relative to the x-axis
    angle = asin((p2.y - p1.y) / length)
    # angle = acos((p2.x - p1.x) / length)
    print("p2.y: ", p2.y, " p1.y: ", p1.y, " angle: ", angle)
    sign = 1
    # if (angle > -90 and angle < 90):
    #     sign = -1
    # else:
    #     sign + 1
    ##  p3 is perpendicular to p1 and p4 is perpendicular to p2
    pg.draw.aaline(surface, color, (p1.x, p1.y), (p2.x, p2.y), 2)
    for i in range(width * 2):
        dx = ((width) - i * 0.5) * cos(angle) * sign
        dy = ((width) - i * 0.5) * sin(angle) * sign
        p3 = Vector(p2.x + dx, p2.y - dy)
        p4 = Vector(p1.x + dx, p1.y - dy)
        pg.draw.aaline(surface, color, (p3.x, p3.y), (p4.x, p4.y), 2)
    pg.draw.circle(surface, 'red', (p1.x, p1.y), 2, 0)
    pg.draw.circle(surface, 'red', (p2.x, p2.y), 2, 0)