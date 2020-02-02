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
GENERALFONT = pg.font.SysFont(None, 200)
DEBUG       = False
FLOOR       = 450 


# Game code begins
p1 = construct("Fighter1.txt")
p2 = construct("Fighter2.txt", True)

while (p1._hp >= 0 and p2._hp >= 0):
    for event in pg.event.get():
        if (event.type == pg.QUIT): 
            pg.quit()
            quit()
    
    PM.movement(p1,p2,event)
    p1.update(FLOOR)
    p2.update(FLOOR)

    GAMEDISPLAY.blit(BACKGROUND, (0, 0))
    pg.draw.rect(GAMEDISPLAY, GOLD, (0, 0, 1280, 70))
    pg.draw.rect(GAMEDISPLAY, BLUE, (10, 10, 630 - 630*(1 - p1._hp/p1._hpfull), 50) if p1._hp else (0,0,0,0))
    pg.draw.rect(GAMEDISPLAY, RED, (630 + 630*(1 - p2._hp/p2._hpfull), 10, 630 - 630*(1 - p2._hp/p2._hpfull), 50))
    if DEBUG:
        pg.draw.rect(GAMEDISPLAY, BLACK, p1.get_hitbox())
        pg.draw.rect(GAMEDISPLAY, WHITE, p2.get_hitbox())
        pg.draw.rect(GAMEDISPLAY, RED, p1.get_activehit())
        pg.draw.rect(GAMEDISPLAY, BLUE, p2.get_activehit())
    GAMEDISPLAY.blit(p1.get_sprite(), p1.get_xy()) # draws image
    GAMEDISPLAY.blit(p2.get_sprite(), p2.get_xy()) 

    pg.display.update() # displays image

GAMEDISPLAY.blit(BACKGROUND, (0, 0))
pg.draw.rect(GAMEDISPLAY, GOLD, (0, 0, 1280, 70))
p1._hp = 0 if p1._hp < 0 else pq._hp
if p1._hp:
    pg.draw.rect(GAMEDISPLAY, BLUE, (10, 10, 630 - 630*(1 - p1._hp/p1._hpfull), 50))
else:
    pg.draw.rect(GAMEDISPLAY, RED, (630 + 630*(1 - p2._hp/p2._hpfull), 10, 630 - 630*(1 - p2._hp/p2._hpfull), 50))
GAMEDISPLAY.blit(p1.get_sprite(), p1.get_xy())
GAMEDISPLAY.blit(p2.get_sprite(), p2.get_xy())

xy  = GENERALFONT.size(("BLUE" if p1._hp else "RED") + " WINS!")
MSG = GENERALFONT.render(("BLUE" if p1._hp else "RED") + " WINS!", True, BLUE if p1._hp else RED)
center = (WINDOWWIDTH/2 - xy[0]/2, WINDOWHEIGHT/2 - xy[1]/2)
GAMEDISPLAY.blit(MSG, center)
pg.display.update()

while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT): 
            pg.quit()
            quit()