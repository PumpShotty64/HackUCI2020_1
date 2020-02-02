# Player Actions

import pygame as pg

def movement(p1, p2, event):

    keys = pg.key.get_pressed()
    p1.set_sprite(0)
    p2.set_sprite(0)


    # Player 1
    if (keys[pg.K_s]): # DOWN
        p1.is_crouching = True;
        p1.set_sprite(1)
    if (keys[pg.K_c]):
        if (p1.is_crouching):
            p1.set_sprite(3)
        else:
            p1.set_sprite(4)
    if (not p1.is_crouching or (p1.is_crouching and p1.is_jumping)):
        if (keys[pg.K_d] and p1.get_xy()[0] >= 0): # RIGHT
            p1.inc_x(p1.SPEED)
            if (not p1.is_crouching): p1.set_sprite(2)
        if (keys[pg.K_a] and p1.get_xy()[0] <= 1280): # LEFT
            p1.inc_x(-p1.SPEED)
            if (not p1.is_crouching): p1.set_sprite(2)
        if (keys[pg.K_w]): # UP
            p1.set_yv(-p1.JUMP)

    if (p1.get_xy()[0] < 0):
        p1.set_x(0)
    if (p1.get_xy()[0] > 1130):
        p1.set_x(1130)


    # Player 2
    if (keys[pg.K_DOWN]): # DOWN
        p2.is_crouching = True;
        p2.set_sprite(1)
    if (keys[pg.K_l]):
        if (p2.is_crouching):
            p2.set_sprite(3)
        else:
            p2.set_sprite(4)
    if (not p2.is_crouching or (p2.is_crouching and p2.is_jumping)):
        if (keys[pg.K_LEFT] and p2.get_xy()[0] <= 1280): # LEFT
            p2.inc_x(-p2.SPEED)
            p2.set_sprite(2)
        if (keys[pg.K_RIGHT] and p2.get_xy()[0] >= -50): # RIGHT
            p2.inc_x(p2.SPEED)
            p2.set_sprite(2)
        if (keys[pg.K_UP]): # UP
            p2.set_yv(-p2.JUMP)
    if (p2.get_xy()[0] < -50):
        p2.set_x(-50)
    if (p2.get_xy()[0] > 1080):
        p2.set_x(1080)


    if not (type(p1).overlap(p1.get_activehit(), p2.get_activehit())):
        if type(p1).overlap(p1.get_activehit(), p2.get_hitbox()):
            p2._hp -= p1._damage
            p2._super += 2*p1._damage
            p1._super += p1._damage
            if p1._damage == 1:
                p2.inc_x(5)
                p2.set_yv(-20)
            else:
                p2.inc_x(5)
                p2.set_yv(-5)
        if type(p1).overlap(p1.get_hitbox(), p2.get_activehit()):
            p1._hp -= p2._damage
            p1._super += 2*p2._damage
            p2._super += p2._damage
            if p2._damage == 1:
                p1.inc_x(-5)
                p1.set_yv(-20)
            else:
                p1.inc_x(-5)
                p1.set_yv(-5)
    
