# main.py

import pygame as pg
import traceback
import random

from Player import Player
from Fighter import Fighter, construct
import Player_Movements as PM

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
BACKGROUND  = pg.transform.scale(pg.image.load("Sprites/tempBack.jpg"), (1280,720))
GENERALFONT = pg.font.SysFont(None, 32)
DEBUGFONT   = pg.font.SysFont(None, 200)
DEBUGGERMSG = DEBUGFONT.render("HELLO", True, WHITE)
FLOOR       = 450 



# Game code begins
try:
    p1 = construct("Fighter1.txt")
    p2 = construct("Fighter2.txt", True)
except:
    input(traceback.format_exc())

while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT): 
            pg.quit()
            quit()
        else:
            print(event.type)

    PM.player_movement(p1, p2)
    p1.update()
    p2.update()

    GAMEDISPLAY.blit(BACKGROUND, (0, 0))
    GAMEDISPLAY.blit(p1.get_sprite(), p1.get_xy()) # draws image
    GAMEDISPLAY.blit(p2.get_sprite(), p2.get_xy()) 


    #GAMEDISPLAY.blit(img2, (400, 100)) # arbitrary position
    pg.display.update() # displays image
