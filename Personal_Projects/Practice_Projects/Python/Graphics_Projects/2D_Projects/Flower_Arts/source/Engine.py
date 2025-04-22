import pygame as pg
import sys
import math


RES = WIDTH, HEIGHT = 1200, 675

SCREEN = pg.display.set_mode(RES)
SURFACE = pg.Surface(RES)
CLOCK = pg.time.Clock()
##  The ordering number of florets
FloretNumber= 0

ScalingParameter = 4

def radToAngle(radValue):
    return (180/math.pi) * radValue

def angleToRad(angle):
    return (math.pi/180) * angle


def drawFlower():

    global FloretNumber, angleOfDivergence, ScalingParameter
    ##  The angle of divergence between consecutive florets, which is constant
    angleOfDivergence = FloretNumber * 137.6
    ##  The distance between centre of flower capitulum and nth floret
    ##  ...not for the radius of the circles used
    radius = ScalingParameter * math.sqrt(FloretNumber)
    
    ##  Polar Coordinates of Consecutive Florets
    x = radius * math.cos(angleToRad(angleOfDivergence)) + WIDTH / 2
    y = radius * math.sin(angleToRad(angleOfDivergence)) + HEIGHT / 2

    """
        Tue-29_Nov_2023
        Explanation of these features:
        
        #1 Problem: I am trying to render each circle in its own surface. Surfaces are normally rectangular or square..,
        But I want the surface to not show, just the circle to show.
        There are two ways to fix this.
        1) Use this definition of the surface:
            pg.Surface((width, height), pg.SRCALPHA)
            pg.SRCALPHA is a flag that makes the surface background transparent.

        2)  Use the set_colorkey((R, G, B)) method
            This method makes any color in the surface that matches the set color key to not be displayed...
            or to be made transparent.
    
    """
    #___M1____#
    # circleSurface = pg.Surface((8, 8), pg.SRCALPHA)
    #_________#
    #___M2___#
    circleRadius = 5
    circleSurface = pg.Surface((circleRadius*2, circleRadius*2))
    circleSurface.fill(pg.Color("yellow"))
    circleSurface.set_colorkey(pg.Color("yellow"))
    #_________#

    color = (100, 255, 255)

    #.circle(surface, color, (x, y), radius, thickness(0=fill, 1=hollow))
    pg.draw.circle(circleSurface,
                    color, (circleRadius, circleRadius), circleRadius, 0)
    ##  This second circle is for the outline of each circle
    pg.draw.circle(circleSurface,
                    pg.Color("black"), (circleRadius, circleRadius), circleRadius, 1)
    ##  This is to offset the surface's position...
    ##  Because normally the position of a surface on another surface is from the top right corner...
    ##  that is, its coordinate that determines its position is not form its center, but the top right corner...
    ##  but I want it to be accurate, to be from the center
    SURFACE.blit(circleSurface, (x-circleRadius, y-circleRadius))
    FloretNumber+=1

    
def display():
    SCREEN.blit(SURFACE, (0, 0))
    drawFlower()
    pg.display.flip()
    CLOCK.tick(60)

def check_events():
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type==pg.KEYDOWN and e.key==pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        

def main():
    SURFACE.fill(pg.Color('darkslategray'))
    while True:
        check_events()
        display()




if __name__ == '__main__':
    main()