from cocos.euclid import *
from cocos.actions import *
from cocos.director import director
from pyglet.window import key
import math

class CustomJump(IntervalAction):

    def init(self, thief_type=None):

        if thief_type == 'fat':
            self.position = (500, 0)
            self.height = 50
            self.duration = 10
            self.jumps = 4

        elif thief_type == 'small':
            self.position = (500, 0)
            self.height = 200
            self.duration = 5
            self.jumps = 2

        elif thief_type == 'tall':
            self.position = (500, 0)
            self.height = 100
            self.duration = 15
            self.jumps = 3

    def start( self ):
        self.start_position = self.target.position
        self.delta = Vector2(*self.position)

    def update(self, t):

        self.target.alive = self.collide( self.target.position, \
                                director.scene.catcher.position )

        if self.target.alive:
            y = self.height * abs( math.sin( t * math.pi * self.jumps ) )
            y = int(y+self.delta[1] * t)
            x = self.delta[0] * t
            self.target.position = self.start_position + Point2(x,y)

        else:
            self.target_position = self.target_position[0], self.target_position[1]-10

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

    def collide((thief_x, thief_y), (catcher_x, catcher_y)):
        print 'Thief pos: ', thief_x, thief_y
        print 'Catcherpos: ', catcher_x, catcher_y
        return True

class CustomMove(Move):

    def step(self, dt):
        keys = director.scene.keys
        catcher = director.scene.catcher
        if keys[key.LEFT] and catcher.position[0] > 300: 
            catcher.position = (catcher.position[0] - catcher.mov_rate, \
                                    catcher.position[1])

        elif keys[key.RIGHT] and catcher.position[0] < 500:
            catcher.position = (catcher.position[0] + catcher.mov_rate, \
                                    catcher.position[1])
