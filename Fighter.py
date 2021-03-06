from Player import Player

import pygame as pg
from LinkedList import LinkedList


def construct(inf, reverse = False):
    # dictionary containing all key value pairs where the keys are
    # the object attribute names in Fighter.__init__ and the values
    # are the coresponding data (see Fighter1.txt for example of
    # data being read in)
    d = {}

    for line in open(inf):
        line = line.rstrip().split("\t")

        # we use a try-except-finally block because entries in the
        # file being read may be in any order. Entries are either
        # integers or filenames to be made into Pygame Surfaces obj.
        try:
            line[1] = int(line[1])
        except:
            line[1] = pg.transform.scale(pg.image.load(line[1]), (200,200))
            line[1] = line[1] if not reverse else pg.transform.flip(line[1], True, False)
            # may affect hitbox math ^^
        finally:
            if isinstance(line[1], int):
                d[line[0]] = line[1]
            elif line[0] in d.keys():
                d[line[0]].append(line[1])
            else:
                d[line[0]] = [line[1]]

    # because walking is a looping animation, we use a linked list
    # to make animation more fluid and efficient
    start   = LinkedList(None, d["walk"][0])
    current = start
    for i in range(1, len(d["walk"])):
        current.next = LinkedList(None, d["walk"][i])
        current = current.next
    current.next = start
    d["walk"] = start

    start   = LinkedList(None, d["pnch"][0])
    current = start
    for i in range(1, len(d["pnch"])):
        current.next = LinkedList(None, d["pnch"][i])
        current = current.next
    current.next = start
    d["pnch"] = start

    # return a fighter containing the data specified in FighterX.txt
    return Fighter(d["hp"],   d["idle"], d["walk"], 
                   d["pnch"], d["kick"], d["crch"], 
                   (d["x"], d["y"]), (d["xv"], d["yv"]), 
                   (d["w"], d["h"]), (d["wb"], d["hb"]),
                   (d["attx"], d["atty"], d["cattx"], d["catty"]),
                   d["sprmx"])



class Fighter(Player):
    WALKBUFFER   = 4
    ATTACKBUFFER = 30
    KICKBUFFER   = 2
    def __init__(self, hp, idle, walk, punch, kick, crouch, xy, xyv, wh, cor, attxy, sprmx):
        self._hp        = hp
        self._hpfull    = hp
        self._super     = 0
        self._supermax  = sprmx
        self._idle      = idle[0]
        self._sprite    = self._idle       # most current sprite to be used
        
        self._walk      = walk             # linked list type
        self._walkFront = walk             # use to reset walking animation
        self._walking   = 0

        self._punch     = punch            # linked list type
        self._pnchFront = punch            # use to reset punching animation

        self._kick      = kick[1]
        self._crouch    = crouch[0]

        self._hitbox    = (xy[0], xy[1], wh[0], wh[1])
        self._hitboxcor = cor
        self._attcor    = (attxy[0], attxy[1], attxy[2], attxy[3])

        self._action    = 0
        self._actionbuf = 0

        self._activeHit = (0,0, 0,0)
        self._damage    = 0

        Player.__init__(self, xy, xyv, wh)

    def get_hitbox(self):
        return self._hitbox

    def set_hitbox(self, tup):
        self._hitbox = tup

    def reset_hitbox(self):
        self._hitbox = (self.get_x() + self._hitboxcor[0], self.get_y() + self._hitboxcor[1], self.get_w(), self.get_h())

    def resetWalk(self):
        self._walk    = self._walkFront
        self._walking = 0

    def resetPunch(self):
        self._punch = self._pnchFront

    def get_activehit(self):
        return self._activeHit

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, sprite):
        if sprite == 0:
            self._sprite = self._idle
            self.is_crouching = False
            self.reset_hitbox()
            self._activeHit = (0, 0, 0, 0)
        if sprite == 1:
            self._sprite = self._crouch
            self.is_crouching = True
            self.set_hitbox( (self.get_x() + self._hitboxcor[0], self.get_y() + self.get_h()/2 + self._hitboxcor[1],
                              self.get_w(), self.get_h()/2) )
        if sprite == 2:
            self._sprite = self._walk.value
            self._walking += 1
            if self.WALKBUFFER == self._walking:
                self._walk    = self._walk.next
                self._walking = 0
        if sprite == 3: 
            self._activeHit = (self.get_x() + self._attcor[0], self.get_y() + self._attcor[1], 50, 50)
            self._sprite = self._kick
            self._damage = 1
        if sprite == 4:
            self._activeHit = (self.get_x() + self._attcor[2], self.get_y() + self._attcor[3], 90, 100)
            self._action = 2
            self._sprite = self._punch.value
            self._actionbuf += 1
            self._damage = 3
            if self._actionbuf > self.ATTACKBUFFER*0.35:
                self._activeHit = (0, 0, 0, 0)
                self._sprite = self._idle
            if self._actionbuf == self.ATTACKBUFFER:
                self._punch = self._punch.next
                self._actionbuf = 0
                self._action = 0
                self._activeHit = (0, 0, 0, 0)

    @staticmethod
    def overlap(h, other):
        if (h[0] + h[2] > other[0] and h[1] + h[3] > other[1]):
            if not (h[0] > other[0] + other[2] or h[1] > other[1] + other[3]):
                return True

    def update(self, floor):
        if self._action == 0:
            self._damage = 0
            Player.update(self, floor)
            if self.get_xv() != 0 and not self.is_jumping:
                self.set_sprite(2)
        if self._action == 1: 
            pass # for special hit
        if self._action == 2:
            Player.update(self, floor)
            self.set_sprite(4)















