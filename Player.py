# Player class. Every player has xy-position, xy-velocity,
# and wh-dimensions (width and height). acceleration may
# simmulated by inc_xv, inc_yv to change xy-velocity

class Player:
    GRAVITY = 1
    SPEED   = 8
    JUMP    = 25

    def __init__(self, xy, xyv, wh):
        self.set_xy(xy)
        self.set_xyv(xyv)
        self.set_dim(wh)
        self.is_jumping   = False
        self.is_crouching = False

    def set_xy(self, xy):
        self._x = xy[0]
        self._y = xy[1]

    def set_xyv(self, xyv):
        self._xv = xyv[0]
        self._yv = xyv[1]

    def set_dim(self, wh):
        self._w = wh[0]
        self._h = wh[1]

    def get_xy(self):
        return (self._x, self._y)

    def get_xyv(self):
        return (self._xv, self._yv)

    def get_dim(self):
        return (self._w, self._h)

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_xv(self, xv):
        self._xv = xv

    def set_yv(self, yv):
        if not self.is_jumping:
            self._yv = yv

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_xv(self):
        return self._xv

    def get_yv(self):
        return self._yv

    def get_w(self):
        return self._w

    def get_h(self):
        return self._h
    
    def inc_x(self, xv):
        self._x += xv
    
    def inc_y(self, yv):
        self._y += yv

    def inc_xv(self, dx):
        self._xv += dx

    def inc_yv(self, dy):
        self._yv += dy

    def update(self, floor):
        self._x += self._xv
        self._y += self._yv
        if (self._y >= floor):
            self._y  = floor
            self._yv = 0
            self.is_jumping = False
        else:
            self.is_jumping = True
            self._yv += Player.GRAVITY