from Player import Player

class Fighter(Player):
    def __init__(self, hp, png, xy, xyv, wh):
        self._hp  = hp
        self._png = png # only one image for now
        Player(self, xy, xyv, wh)

    # box = ((left, top), (right, bottom))
    def attack(self, dmg, box, ph):
        pass

    def overlap(self, other):
        if (self._x + self._w) > other[0][0] and (self._y + self._h) > other[0][1]:
            print("OVERLAP")
            return True



