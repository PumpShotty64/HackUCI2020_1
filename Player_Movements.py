# Player Actions

import pygame as pg

def player_movement():
	keys = pg.key.get_pressed()
	if (keys[pg.K_a]): # LEFT
		print("LEFT")
	elif (keys[pg.K_s]): # DOWN
		print("DOWN")
	elif (keys[pg.K_d]): # RIGHT
		print("RIGHT")
	elif (keys[pg.K_w]): # UP
		print("UP")
