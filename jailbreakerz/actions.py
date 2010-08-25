from cocos.euclid import *
from cocos.actions import *
from cocos.director import director
import math

class CustomJump(IntervalAction):

    def init(self, position, height, jumps, duration):

        self.position = position
        self.height = height
        self.duration = duration
        self.jumps = jumps

    def start( self ):
        self.start_position = self.target.position
        self.delta = Vector2(*self.position)

    def update(self, t):
        y = self.height * abs( math.sin( t * math.pi * self.jumps ) )
        y = int(y+self.delta[1] * t)
        x = self.delta[0] * t
        self.target.position = self.start_position + Point2(x,y)
        print 'updating..'

    def __reversed__(self):
        return CustomJump( (-self.position[0],-self.position[1]), self.height, self.jumps, self.duration)

    def step(self, dt):
        self._elapsed += dt
        try:
            self.update( min(1, self._elapsed/self.duration ) )
        except ZeroDivisionError:
            self.update(1.0)

    def done(self):
        return self._elapsed >= self.duration


