"""
    This is my version of the Forward Kinematics tutorial
"""

import pygame as pg
import math
import random as rndm
from Core.Graphics import *


class Segment:
            ##  The angle is relative to thte x-axis
    def __init__(self, length, angle, color=(255, 255, 255)):
        self.p1 = Vector(0, 0)
        self.p2 = Vector(0, 0)
        self.length = length
        ##  Angle is always relative to x-axis
        self.angle = angle
        self.orientation_angle = angle
        self.amplitude_of_motion = 0
        self.dx, self.dy = 0.0, 0.0
        self.direction = 0.0
        self.color = color
        self.parent_segment = None
        self.child_segment = None


    def on_init(self):
        ...

    def set_child(self):
        ...

    def calculate_point2(self):
       ##   Becuase y-axis for pygame is inverted, as in, going down is positive, and the top left corner is 0, 0...
       ##   I do self.p1.y - self.dy
        self.p2 = Vector(self.p1.x + self.dx, self.p1.y - self.dy)
    
    ##  The things to be updated regularly
    def update(self):
        ...

    def draw(self, surface, width = 1):
        self.update()
        # pg.draw.aaline(surface, self.color, (self.p1.x,self.p1.y), (self.p2.x, self.p2.y), width)
        drawLine(surface, self.color, (self.p1.x, self.p1.y), (self.p2.x, self.p2.y), width)
        

class SegmentAnchor(Segment):
    ##  For the anchor segment, point 1 is fixed, point 2 rotates
    def __init__(self, x, y, length, angle, color=(255, 255, 255), amplitude=30):
        super().__init__(length, angle, color)
        self.p1 = Vector(x, y)
        self.on_init(amplitude)

    def on_init(self, amplitude):
        self.amplitude_of_motion = amplitude
        self.calculate_direction()
        self.calculate_point2()

    def set_child(self, child):
        self.child_segment = child

    def calculate_direction(self):
        self.dx, self.dy = self.length * cos(self.angle), self.length * sin(self.angle)
        ##  Direction is relative to the point1, away from it; a unit vector.
        self.direction = self.dy / self.dx

    def move_end(self):
        dt = pg.time.get_ticks() * 0.001
        self.angle = self.amplitude_of_motion * sin(100 * dt) + self.orientation_angle

    def update(self):
        self.calculate_direction()
        self.calculate_point2()


        
class SegmentBody(Segment):
    def __init__(self, length, angle, parent, color=(255,255,255)):
        super().__init__(length, angle, color)
        self.on_init(parent)
    
    def on_init(self, parent):
        self.parent_segment = parent
        self.amplitude_of_motion = 0.75 * self.parent_segment.amplitude_of_motion
        ##  Set p1 from parent
        self.p1=Vector(self.parent_segment.p2.x, self.parent_segment.p2.y)
        self.calculate_direction()
        self.calculate_point2()

    def set_child(self, child):
        self.child_segment = child

    def calculate_direction(self):
        self.dx, self.dy = self.length * cos(self.angle), self.length * sin(self.angle)
        ##  Direction is relative to the point1, away from it; a unit vector.
        self.direction = self.dy / self.dx
    
    def update_orientation(self):
        """
            Behind the math here.
            a * -cos(100*dt) + c
            a = amplitude: it determines the max and min angle range that the segment oscillates through; a = 45
            c = displacement. It dipaces the angle to stand in the right orientation. Normally, the angle is set at 45 on initializing.
            Setting the angle to the function below to update it, giving the parent angle as the starting angle makes it...
            oscillate in the right range of angles for the right orientation.
            the trig part is made negative for a reason:
            so that its motion is opposite that of the base or parent segment
            so when the parent segment is goinf right, it goes left, and when the parent goes left, it goes right.
        """
        self.orientation_angle = self.parent_segment.angle
        dt = pg.time.get_ticks() * 0.001
        # self.angle += self.parent_segment.angle + 15*cos(10*dt) + 45
        self.angle =  self.amplitude_of_motion * -cos(100*dt) + self.orientation_angle
        self.calculate_direction()

    def update_point1(self):
        ##  The point1 must always be attached to the point2 of the segment before it
        self.p1.x, self.p1.y = self.parent_segment.p2.x, self.parent_segment.p2.y

    def update(self):
        self.update_orientation()
        self.update_point1()
        self.calculate_point2()


    
class Tentacle:
    def __init__(self, surface, pos,numberOfSegments, avg_size=100):
        self.render_surface = surface
        self.tentacle = []
        self.average_size = avg_size
        self.anchor_segment = SegmentAnchor(pos[0], pos[1], self.average_size, 90, color=self.get_colour(rndm.randint(0, numberOfSegments)))
        self.make_tentacle(numberOfSegments)
        self.color = (255, 255, 255)
        
    
    def set_colour(self, variable):
        self.color = (rndm.randrange(125, 255, (variable+1) * 2), rndm.randrange(125, 255, (variable + 1) * 2), rndm.randrange(125, 255, (variable + 1) * 2))

    def get_colour(self, variable):
        return (rndm.randrange(125, 255, (variable+1) * 2), rndm.randrange(125, 255, (variable + 1) * 2), rndm.randrange(125, 255, (variable + 1) * 2))

    def make_tentacle(self, numberOfSegments):
        self.tentacle.append(self.anchor_segment)
        #3  Minus 1 because the anchor_segment has already been added
        for count in range(numberOfSegments-1):
            self.set_colour(count)
            currentSegment = SegmentBody(self.average_size -(2.5 * count), 90, parent=self.tentacle[count], color=self.color)
            self.tentacle[count].set_child(currentSegment);
            self.tentacle.append(currentSegment)
            
    def draw(self):
        self.tentacle[0].move_end()
        for segment in self.tentacle:
            segment.draw(self.render_surface, 5)

            


class ForwardKinematics:

    def __init__(self, engine):
        print("Forward Kinematics")
        self.engine = engine

        # self.anchor_segment = SegmentAnchor(500, 500, 100, 90)
        # self.body_segment = SegmentBody(100, 90,self.anchor_segment)
        self.tentacles = []
        self.tentacle_field()

    def tentacle_field(self):
        for i in range(50): 
            tentacle = Tentacle(self.engine.screen,(rndm.randint(250, 500), (rndm.randint(250,500))), 5, avg_size=45)
            self.tentacles.append(tentacle)


    def display(self):
        # self.anchor_segment.move_end()
        # self.anchor_segment.draw(self.engine.screen, 5)
        # self.body_segment.draw(self.engine.screen, 5)

        for tentacle in self.tentacles:
            tentacle.draw()
        


        