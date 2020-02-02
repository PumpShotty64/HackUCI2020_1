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
        if (keys[pg.K_d]): # RIGHT
            p1.inc_x(p1.SPEED)
            if (not p1.is_crouching): p1.set_sprite(2)
        if (keys[pg.K_a]): # LEFT
            p1.inc_x(-p1.SPEED)
            if (not p1.is_crouching): p1.set_sprite(2)
        if (keys[pg.K_w]): # UP
            p1.set_yv(-p1.JUMP)


    # Player 2
    if (keys[pg.K_LEFT]): # LEFT
        p2.inc_x(-p2.SPEED)
        p2.set_sprite(2)
    if (keys[pg.K_RIGHT]): # RIGHT
        p2.inc_x(p2.SPEED)
        p2.set_sprite(2)

    # overlapping boxes
    if type(p1).overlap(p1.get_hitbox(), p2.get_hitbox()):
        # make them both stop moving
        pass

    if not type(p1).overlap(p1.get_activehit(), p2.get_activehit()):
        if type(p1).overlap(p1.get_activehit(), p2.get_hitbox()):
            p2._hp -= p1._damage
            print("take damage!")
        if type(p1).overlap(p1.get_hitbox(), p2.get_activehit()):
            p1._hp -= p2._damage
    
