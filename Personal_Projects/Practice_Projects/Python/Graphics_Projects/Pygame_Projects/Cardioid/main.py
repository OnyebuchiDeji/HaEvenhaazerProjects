import pygame as pg
import math

class Cardioid:
    def __init__(self, app): # Takes an instance of the App class
        self.app = app
        self.radius = 320
        self.num_lines = 200
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
        self.counter, self.inc = 0, 0.01

    def get_colour(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else(
            max(min(self.counter, 1), 0), -self.inc)
        
        return pg.Color('red').lerp('green', self.counter)

    def GrowingCardioid(self):
        #   Using the function y = abs(sin(x) - 0.5) to imitate heart beat of cardioid
        time = pg.time.get_ticks()  #   Taking the number of milliseconds since start of application
        self.radius = 280 + 50 * abs(math.sin(time * 0.004) - 0.5)

        #   This variable increases with time
        factor = 1 + 0.0001 * time
        
        for i in range(self.num_lines):
            #   Calculating the angle between the center line and next point made by lines traced through them from center...
            #   And multiplying by i, which will give the angle between the center point and next point
            theta = (2 * math.pi / self.num_lines) * i

            #   Then calculate the same point's coordinates using sine and cosine
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            # Calculating next point's angle
            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta))  + self.translate[1]

            pg.draw.aaline(self.app.screen, 'green', (x1, y1), (x2, y2))
    
    def colouredGrowingCardioid(self):
        #   Using the function y = abs(sin(x) - 0.5) to imitate heart beat of cardioid
        time = pg.time.get_ticks()  #   Taking the number of milliseconds since start of application
        self.radius = 280 + 50 * abs(math.sin(time * 0.004) - 0.5)

        #   This variable increases with time
        factor = 1 + 0.0001 * time
        
        for i in range(self.num_lines):
            #   Calculating the angle between the center line and next point made by lines traced through them from center...
            #   And multiplying by i, which will give the angle between the center point and next point
            theta = (2 * math.pi / self.num_lines) * i

            #   Then calculate the same point's coordinates using sine and cosine
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            # Calculating next point's angle
            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta))  + self.translate[1]

            pg.draw.aaline(self.app.screen, self.get_colour(), (x1, y1), (x2, y2))

    def draw(self):
        self.drawAnother()
        


#  Simple template for working with pygame library
class App:
    def __init__(self):
        self.screen = pg.display.set_mode([1280, 720])
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw(self):
        self.screen.fill('black')
        self.cardioid.draw()
        pg.display.flip()       #   Update screen

    def run(self):
        #   Main loop
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)

if __name__ == '__main__':
    app = App()
    app.run()