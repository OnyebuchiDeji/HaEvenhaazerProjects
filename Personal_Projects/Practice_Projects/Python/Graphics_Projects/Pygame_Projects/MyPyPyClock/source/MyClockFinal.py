import pygame as pg
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
RADIUS_ARK = RADIUS + 8

radius_list = {'sec':RADIUS - 10, 'min': RADIUS - 55, 'hour':RADIUS - 100, 'digit': RADIUS - 30}

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()


clock12 = dict(zip(range(12), range(0, 360, 30)))   ##  Hour hand
clock60 = dict(zip(range(60), range(0, 360, 6)))    ##  For minutes and second

font = pg.font.SysFont('Verdana', 60)
img = pg.image.load('Resources/2.png').convert_alpha()
bg = pg.image.load('Resources/bg4.jpg').convert()
##  Because loaded images get surfaces, they have a get_rect method/attribute
bg_rect = bg.get_rect()
bg_rect.center = WIDTH, HEIGHT
dx, dy = 1, 1 


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            exit()
    
    #   Set Background
    ##surface.fill(pg.Color('black'))
    dx *= -1 if bg_rect.left > 0 or bg_rect.right < WIDTH else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < HEIGHT else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    surface.blit(bg, bg_rect)
    surface.blit(img, (0, 0))

    ##  Get Current Time
    current_time = datetime.now()

    ##  This was re-written because the hour arm could not appear between the hours, like when it is 20:30...
    ##  the hour arm should be between 20:00 and 21:00
    ##_________________________________________________##
    ## Was: hour, minute, second = current_time.hour % 12, current_time.minute, current_time.second
    ##_________________________________________________##
    hour, minute, second = ((current_time.hour % 12) * 5 + current_time.minute // 12) % 60, current_time.minute, current_time.second

    ##  Draw Face
    ##pg.draw.circle(surface, pg.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)

    for digit, pos in clock60.items(): 
        ##  Because of the change 
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pg.draw.circle(surface, pg.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)

    ##  Draw Clock

    ##pg.draw.circle(surface, pg.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pg.draw.line(surface, pg.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pg.draw.line(surface, pg.Color('violet'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 8)
    pg.draw.line(surface, pg.Color('red'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pg.draw.circle(surface, pg.Color('white'), (H_WIDTH, H_HEIGHT), 8)


    #   Digital Clock
    time_render = font.render(f'{current_time:%H:%M:%S}', True, pg.Color('skyblue'), pg.Color('black'))
    surface.blit(time_render, (0, 0))

    #   Draw Arc
    sec_angle = -math.radians(clock60[current_time.second]) + math.pi / 2
    pg.draw.arc(surface, pg.Color('gold'),
                (H_WIDTH - RADIUS_ARK, H_HEIGHT - RADIUS_ARK, 2 * RADIUS_ARK, 2 * RADIUS_ARK),
                math.pi / 2, sec_angle, 8)

    ##  Update Surface
    pg.display.flip()
    ##  To maintain framerate
    clock.tick(60)
