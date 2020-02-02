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

    # return a fighter containing the data specified in FighterX.txt
    return Fighter(d["hp"],   d["idle"], d["walk"], 
                   d["pnch"], d["kick"], d["crch"], 
                   (d["x"], d["y"]), (d["xv"], d["yv"]), (d["w"], d["h"]))



class Fighter(Player):
    WALKBUFFER = 4
    def __init__(self, hp, idle, walk, punch, kick, crouch, xy, xyv, wh):
        self._hp        = hp
        self._idle      = idle[0]
        self._walk      = walk             # linked list type
        self._punch     = tuple(punch)
        self._kick      = tuple(kick)
        self._crouch    = crouch[0]
        self._sprite    = self._idle       # most current sprite to be used
        self._walkFront = walk             # use to reset walking animation
        self._walking   = 0
        Player.__init__(self, xy, xyv, wh)

    def get_sprite(self):
        return self._sprite

    def resetWalk(self):
        self._walk = self._walkFront
        self._walking = 0

    # box = ((left, top), (right, bottom))
    def attack(self, dmg, box, ph):
        pass

    def overlap(self, other):
        if (self._x + self._w) > other[0][0] and (self._y + self._h) > other[0][1]:
            print("OVERLAP")
            return True

    def set_sprite(self, sprite):
        if sprite == 0:
            self._sprite = self._idle
            self.is_crouching = False
        if sprite == 1:
            self._sprite = self._crouch
            self.is_crouching = True
        if sprite == 2:
            self._sprite = self._walk.value
            self._walking += 1
            if self.WALKBUFFER == self._walking:
                self._walk = self._walk.next
                self._walking = 0
        if sprite == 3: 
            pass # kick
        if sprite == 4:
            pass # punch

    def update(self, floor):
        Player.update(self, floor)
        if self.get_xv() != 0 and not self.is_jumping:
            self.set_sprite(2)















