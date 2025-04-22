import pygame as pg
from datetime import datetime


RES = WIDTH, HEIGHT = 1280, 675

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

font = pg.font.SysFont('Verdeba', 200)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    #   Set Background
    surface.fill(pg.Color('black'))
    #   Get time
    current_time =  datetime.now()
    #   draw clock
    time_render = font.render(f'{current_time:%H:%M:%S}', True, pg.Color('skyblue'), pg.Color('black'))
    surface.blit(time_render, (WIDTH//2, HEIGHT//2))

    pg.display.flip()
    clock.tick(60)
