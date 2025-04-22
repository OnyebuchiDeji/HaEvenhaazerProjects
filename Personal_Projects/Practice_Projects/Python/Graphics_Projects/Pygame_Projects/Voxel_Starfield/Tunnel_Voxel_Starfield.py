import pygame as pg
import random
import math

vec2, vec3 = pg.math.Vector2, pg.math.Vector3

RES = WIDTH, HEIGHT = 1200, 675     	##  16:9
NUM_STARS = 2000    ##  was 1500
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = 'blue skyblue cyan purple magenta violet white'.split()
##  The below indicates the distance along the Z axis from which the stars will begin to move
Z_DISTANCE = 140    ##  was 40
ALPHA = 30          ##  was 100


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_tunnel_pos3d()
        self.vel = random.uniform(0.45, 0.95)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    def get_tunnel_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        ##  Random radius to get random positions of the stars
        ##  radius = random.randrange(HEIGHT)   ##
        ##  This increases the range of star field by increasing the range of possible radii...
        ##  each star can get, so making the range of possible positions wider
        radius = random.randrange(HEIGHT // 4, HEIGHT // 3) * scale_pos
        ##  USing polar coordinates to get the star's position
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)

        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_tunnel_pos3d() if self.pos3d.z < 1 else self.pos3d

        ##  Applying 3d projection to 2d screen space
        ##  Each x and y value is gotten independent of the center in get_pos3d()...
        ##  therefore, here, it is offset from the center of the screen...
        ##  so that the stars can appear to be moving from the center
        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        ##  was: self.size = Z_DISTANCE / self.pos3d.z  ##
        self.size = (Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z)
        #   Rotate x, y Plane
        self.pos3d.xy = self.pos3d.xy.rotate(0.2)
        #   Use Mouse
        mouse_pos = CENTER - vec2(pg.mouse.get_pos())
        self.screen_pos += mouse_pos

    def draw(self):
        pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))
        
class StarField:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)]

    def run(self):
        [star.update() for star in self.stars]
        ##  The painter's algorithm: makes sure the objects behind do not appear of the ones in front
        ##  by drawing the ones in front first
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.alpha_surface = pg.Surface(RES)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = StarField(self)

    def run(self):
        while True:
            # self.screen.fill('black')
            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()

            pg.display.flip()
            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            self.clock.tick(60)
        

if __name__ == '__main__':
    app = App()
    app.run()