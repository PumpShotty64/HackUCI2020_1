# main.py

import pygame as pg
import traceback
import random

from Player import Player

# Pygame constaants
WINDOWWIDTH  = 1280
WINDOWHEIGHT = 720
RESOLUTION   = (WINDOWWIDTH, WINDOWHEIGHT)
WINDOWNAME   = "HackUCI2020"
WHITE        = (255, 255, 255)
BLACK        = (0, 0, 0)

# Pygame setup
pg.init()
# pg.display.set_icon(pg.image.load("someImage.png"))
pg.display.set_caption(WINDOWNAME)
GAMEDISPLAY  = pg.display.set_mode(RESOLUTION)
CLOCK        = pg.time.Clock()

# Game constants
# BACKGROUND  = pg.image.load("")
GENERALFONT = pg.font.SysFont(None, 32)
DEBUGFONT   = pg.font.SysFont(None, 200)
DEBUGGERMSG = DEBUGFONT.render("HELLO", True, WHITE)
FLOOR       = 700  # arbitrary number

# Game code begins

p1 = Player((100, 100), (0, 0), (30, 60))

while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT): 
            pg.quit()
            quit()
        else:
            print(event.type)
    GAMEDISPLAY.blit(DEBUGGERMSG, (100, 100)) # arbitrary position
    pg.display.update()
