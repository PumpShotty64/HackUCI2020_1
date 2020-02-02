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
RED          = (255, 0, 0)
BLUE         = (0, 0, 255)
GOLD         = (212, 175, 55)


# Pygame setup
pg.init()
# pg.display.set_icon(pg.image.load("someImage.png"))
pg.display.set_caption(WINDOWNAME)
GAMEDISPLAY  = pg.display.set_mode(RESOLUTION)
CLOCK        = pg.time.Clock()

# Game constants
BACKGROUND  = pg.transform.scale(pg.image.load("Sprites/background.png"), (1280,720))
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
    
    PM.movement(p1,p2,event)
    p1.update(FLOOR)
    p2.update(FLOOR)

    GAMEDISPLAY.blit(BACKGROUND, (0, 0))
    pg.draw.rect(GAMEDISPLAY, GOLD, (0, 0, 1280, 70))
    pg.draw.rect(GAMEDISPLAY, BLUE, (10, 10, 620 - 630*(1 - p1._hp/p1._hpfull), 50))
    pg.draw.rect(GAMEDISPLAY, RED, (630 + 620*(1 - p2._hp/p2._hpfull), 10, 630, 50))
    pg.draw.rect(GAMEDISPLAY, BLACK, p1.get_hitbox())
    pg.draw.rect(GAMEDISPLAY, WHITE, p2.get_hitbox())
    GAMEDISPLAY.blit(p1.get_sprite(), p1.get_xy()) # draws image
    GAMEDISPLAY.blit(p2.get_sprite(), p2.get_xy()) 
    pg.draw.rect(GAMEDISPLAY, RED, p1.get_activehit())


    #GAMEDISPLAY.blit(img2, (400, 100)) # arbitrary position
    pg.display.update() # displays image
