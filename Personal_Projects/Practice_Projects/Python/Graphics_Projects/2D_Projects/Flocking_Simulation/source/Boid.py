import pygame as pg
import math
import random as rnd

from Math_Structures import *

"""
    Alignment
    Cohesion
    Separation
    
"""
class Boid:
    def __init__(self, surface: pg.Surface, pos:Vec2 = Vec2(0, 0)):
        self.surface_ref = surface
        self.position = pos
        self.radius = 5
        self.velocity = Vector().random2D(-10, 10)
        self.velocity.setMag(rnd.random()*4)
        self.acceleration = Vec2(0, 0)
        self.max_steer_force = 0.2
        self.max_speed = 2

        # self.color = (rnd.randrange(32, 64), rnd.randrange(16, 32), rnd.randrange(102, 255))
        self.color = (255, 255, 255)


    def draw(self):
        pg.draw.circle(self.surface_ref, self.color, (self.position.x, self.position.y), self.radius, width=0)

    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.setMag(self.max_speed)
        # print("Boid Position: ", self.position.x, ", ", self.position.y)
        # print("Boid Velocity: ", self.velocity.x, ", ", self.velocity.y)

    def flock(self, boids: list["Boid"]):
        ##  The acceleration is could be reset to zero so that the new acceleration is gotten every iteration.
        # self.acceleration.mul(0)
        aligning_force = self.align(boids)
        cohesion_force = self.cohesion(boids)
        seperation_force = self.separation(boids)
        self.acceleration.add(seperation_force)
        self.acceleration.add(aligning_force)
        self.acceleration.add(cohesion_force)
        

    def edge_detection(self, screen_width, screen_height):
        ##  This is to make the boids that flow out of one end of the screen...
        ##  to flow back in through the other
        if (self.position.x > screen_width):
            self.position.x = 0
        elif (self.position.x < 0):
            self.position.x = screen_width
        if (self.position.y > screen_height):
            self.position.y = 0
        elif (self.position.y < 0):
            self.position.y = screen_height
        
            
    
    def align(self, boids: list["Boid"]) -> Vec2:
        """
            The goal is to align this boid to the rest of the flock.
            By getting the average velocity vector that is aligned to the flock withing perception.
            Then it returns the Vec2
        """
        ##  Perception is in a circle
        perception_radius = 50;
        ##  Keeps count of the number of vectors checked
        total = 0

        ##  The average velocity is the desired velocity
        ##  This acts as the steering force.
        desired_avg_vel = Vec2()
        for other in boids:
            ##  Only average for the resultant velocity vector from the surrounding boids
            dist_btw = self.position.distance_to(other.position)
            if ((self != other) and (dist_btw < perception_radius)):
                desired_avg_vel.add(other.velocity)
                total += 1

        ##  To get the average velocity of all boids
        if total > 0:
            desired_avg_vel.div(total)
            desired_avg_vel.setMag(self.max_speed)
            desired_avg_vel.sub(self.velocity)
            desired_avg_vel.setMag(self.max_steer_force)
        ##  If nothing is found, a zero vector is returned
        return desired_avg_vel
    
    def cohesion(self, boids: list["Boid"]) -> Vec2:
        """
            The goal is to stir toward the position of the other boids... not their velocity...
            since cohesion means to come together.
        """
        ##  Perception is in a circle
        perception_radius = 50;
        ##  Keeps count of the number of vectors checked
        total = 0

        ##  The average velocity is the desired velocity
        ##  This acts as the steering force.
        desired_avg_location = Vec2()
        for other in boids:
            ##  Only average for the resultant velocity vector from the surrounding boids
            dist_btw = self.position.distance_to(other.position)
            if ((self != other) and (dist_btw < perception_radius)):
                desired_avg_location.add(other.position)
                total += 1

        ##  To get the average location
        ##  To steer toward the average loaction, get the average location and subtract it from the boids...
        ##  current position
        if total > 0:
            desired_avg_location.div(total)
            desired_avg_location.sub(self.position)
            ##  Desired velocity
            desired_avg_location.setMag(self.max_speed)
            ##  Subtract from current velocity
            desired_avg_location.sub(self.velocity)
            ##  Limit the current velocity to max force
            desired_avg_location.setMag(self.max_steer_force)
        ##  If nothing is found, a zero vector is returned
        return desired_avg_location
    

    def separation(self, boids: list["Boid"]) -> Vec2:
        """
            The goal is to stir away the position of the other boids... not their velocity...
            since separation means to move apart.
        """
        ##  Perception is in a circle
        perception_radius = 50;
        ##  Keeps count of the number of vectors checked
        total = 0

        ##  The average velocity is the desired velocity
        ##  This acts as the steering force.
        desired_avg_location = Vec2()
        for other in boids:
            ##  Only average for the resultant velocity vector from the surrounding boids
            dist_btw = self.position.distance_to(other.position)
            
            if ((self != other) and (dist_btw < perception_radius)):
                ##  Gets a vector that points away from the surrounding or local boid
                ##  it is needed to point away from where that boid is
                difference: Vec2 = Vector.sub(self.position, other.position)
                difference.div(dist_btw)
                desired_avg_location.add(difference)
                total += 1

        ##  In this one, position is not subtracted.
                ##  It is only velocity, since it involves steering away from surrounding boids
        if total > 0:
            desired_avg_location.div(total)

            ##  Desired velocity
            desired_avg_location.setMag(self.max_speed)
            ##  Subtract from current velocity
            desired_avg_location.sub(self.velocity)
            ##  Limit the current velocity to max force
            desired_avg_location.setMag(self.max_steer_force)

        ##  If nothing is found, a zero vector is returned
        return desired_avg_location




