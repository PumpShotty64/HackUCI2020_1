# Player Actions

import pygame as pg

def player_movement(p1, p2):

	keys = pg.key.get_pressed()

	if (keys[pg.K_a]): # LEFT
		p1.set_xv(-5)
	elif (keys[pg.K_s]): # DOWN
		pass
	elif (keys[pg.K_d]): # RIGHT
		pass
	elif (keys[pg.K_w]): # UP
		pass
