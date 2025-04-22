"""
    This is the first part of the kinematics tutorial.
    Forward Kinematics
"""

import pygame as pg
import math
from Core.Graphics import *


class Segment:
            ##  The angle is relative to thte x-axis
    def __init__(self, x, y, length, angle, color=(255, 255, 255), parent=None):
        self.p1 = Vector(x, y)
        self.p2 = Vector(0, 0)
        self.length = length
        self.angle = angle
        self.self_angle = self.angle
        # self.
        self.dx, self.dy = 0.0, 0.0
        self.parent_segment = parent
        self.child_segment = None

        self.on_init()

        self.color = color


    def on_init(self):
        """
            on_init() has to call the update method to calculate the second point, p2.
            This is needed especially when each object needs to keep track of its parent object...
            because its p1 has to be initialized from the p2 of its child
        """
        self.update()

    def update_orientation(self):
        self.angle = self.self_angle
        if self.parent_segment != None:
            self.angle += self.parent_segment.angle
        # else:
        #     self.wiggle_end()




    def update_point1(self):
        """
            This method updates the p1 of the current 
        """
        if self.parent_segment != None:
            self.p1.x, self.p1.y = self.parent_segment.p2.x, self.parent_segment.p2.y

    def calculate_point2(self):
       ##   Becuase y-axis for pygame is inverted, as in, going down is positive, and the top left corner is 0, 0
        self.p2 = Vector(self.p1.x + self.dx, self.p1.y - self.dy)
    
    ##  The things to be updated regularly
    def update(self):
        self.dx, self.dy = self.length * cos(self.angle), self.length * sin(self.angle)
        ##  This makes sure to update the p1 of any segment that has a moving parent
        self.update_point1()
        self.calculate_point2()
        self.update_orientation()


    def draw(self, surface, width = 1):
        self.update()
        # pg.draw.aaline(surface, self.color, (self.p1.x,self.p1.y), (self.p2.x, self.p2.y), width)
        drawLine(surface, self.color, (self.p1.x, self.p1.y), (self.p2.x, self.p2.y), width)
        

class ForwardKinematics:

    def __init__(self, engine):
        print("Forward Kinematics")
        self.engine = engine
        # self.seg1 = Segment(500, 200, 255, -45);
        # self.seg2 = Segment(500, 200, 100, 0, parent=self.seg1);
        self.anchor_segment = Segment(500, 250, 100, 90)
        self.tentacle = []
        self.on_init()


        
    def on_init(self):
        self.tentacle.append(self.anchor_segment)
        for i in range(2):
            current = Segment(500, 250, 100, 45, parent=self.tentacle[i])
            self.tentacle[i].child = current;
            self.tentacle.append(current)
        

    def update(self):
        ...

    def display(self):
        # self.seg1.rotate_end()
        # self.seg1.draw(self.engine.screen, width=10)
        # self.tentacle[0].move_end()
        for segment in self.tentacle:
            segment.draw(self.engine.screen, width = 3)


        