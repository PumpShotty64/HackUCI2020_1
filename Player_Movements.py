# Player Actions

import pygame as pg

def movement(p1, p2, event):
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_a): # LEFT
            p1.inc_xv(-p1.SPEED)
        if (event.key == pg.K_s): # DOWN
            p1.set_sprite(1)
        if (event.key == pg.K_d): # RIGHT
            p1.inc_xv(p1.SPEED)
        if (event.key == pg.K_w): # UP
            p1.set_yv(-p1.JUMP)
    else:
        if (event.key == pg.K_a): # LEFT
            p1.inc_xv(p1.SPEED)
        if (event.key == pg.K_s): # DOWN
            p1.set_sprite(0)
        if (event.key == pg.K_d): # RIGHT
            p1.inc_xv(-p1.SPEED)
        if (event.key == pg.K_w): # UP
            pass