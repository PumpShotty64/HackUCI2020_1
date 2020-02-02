# Player Actions

import pygame as pg

def movement(p1, p2, event):

    keys = pg.key.get_pressed()
    p1.set_sprite(0)
    p2.set_sprite(0)

    if (keys[pg.K_a]): # LEFT
        p1.inc_x(-p1.SPEED)
        p1.set_sprite(2)
    if (keys[pg.K_d]): # RIGHT
        p1.inc_x(p1.SPEED)
        p1.set_sprite(2)


    if (keys[pg.K_LEFT]): # LEFT
        p2.inc_x(-p2.SPEED)
        p2.set_sprite(2)
    if (keys[pg.K_RIGHT]): # RIGHT
        p2.inc_x(p2.SPEED)
        p2.set_sprite(2)


    # if (event.type == pg.KEYDOWN):
    #     if (event.key == pg.K_a): # LEFT
    #         p1.inc_xv(-p1.SPEED)
    #     if (event.key == pg.K_s): # DOWN
    #         p1.set_sprite(1)
    #     if (event.key == pg.K_d): # RIGHT
    #         p1.inc_xv(p1.SPEED)
    #     if (event.key == pg.K_w): # UP
    #         p1.set_yv(-p1.JUMP)
    # else:
    #     if (event.key == pg.K_a): # LEFT
    #         p1.inc_xv(p1.SPEED)
    #     if (event.key == pg.K_s): # DOWN
    #         p1.set_sprite(0)
    #     if (event.key == pg.K_d): # RIGHT
    #         p1.inc_xv(-p1.SPEED)
    #     if (event.key == pg.K_w): # UP
    #         pass
