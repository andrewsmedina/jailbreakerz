from cocos.euclid import *
from cocos.actions import *
from cocos.director import director

from pyglet.window import key

from message import MessageScene

import score
import math

def collide(a, b):
    distance = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    return distance < (a.width/2 + b.width/2)
    
def collide_on_trampoline(a, b):
    x_center_a = a.x + (a.width/2)
    return a.y < 150 and x_center_a > b.x and x_center_a < b.x + b.width
            
class CustomJump(IntervalAction):

    def freedom_checking(self):
        if not self.freedom and collide(self.target, director.scene.kombi):
            score.score_points += 10
            self.freedom = True
    
    def dead_checking(self):
        if not self.freedom and not self.is_dead and self.target.y < -30:
            director.replace(MessageScene('GAME OVER'))
            self.is_dead = True
    
    def saved(self):
        if not self.freedom and collide_on_trampoline(self.target, director.scene.catcher):
            return True
        
        return False
        
        #if not self.freedom and collide(self.target, director.scene.catcher):
        #    return True
        
        #return False
            #self.stop()

    def init(self, thief_type=None):
        
        self.thief_type = thief_type
        
        self.freedom = False
        self.is_dead = False

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
            
        self.jumps = 1
        self.height = 200
        self.duration = 3
        self.position = (200, -250)


    def start( self ):
        self.start_position = self.target.position
        self.delta = Vector2(*self.position)
        
    def update(self, t):
        self.dead_checking()
        self.freedom_checking()
            
        
        if self.saved():
            print 'SAVED'
            #self.target.do(CustomJump(self.thief_type))
            # inverte jump ou rejump

        y = self.height * abs( math.sin( t * math.pi * self.jumps ) )
        y = int(y+self.delta[1] * t)
        x = self.delta[0] * t
        
        self.target.position = self.start_position + Point2(x,y)

            

        # self.target.alive = self.collide( self.target.position, \
        #                         director.scene.catcher.position )
        # 
        # if self.target.alive:
        #     y = self.height * abs( math.sin( t * math.pi * self.jumps ) )
        #     y = int(y+self.delta[1] * t)
        #     x = self.delta[0] * t
        #     self.target.position = self.start_position + Point2(x,y)
        # 
        # else:
        #     self.target_position = self.target_position[0], self.target_position[1]-10

    def __reversed__(self):
        return CustomJump( (-self.position[0],-self.position[1]), self.height, self.jumps, self.duration)
    # 
    # def step(self, dt):
    #     self._elapsed += dt
    #     try:
    #         self.update( min(1, self._elapsed/self.duration ) )
    #     except ZeroDivisionError:
    #         self.update(1.0)
    # 
    # def done(self):
    #     return self._elapsed >= self.duration

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
