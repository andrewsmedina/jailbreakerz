from cocos.sprite import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
from pyglet import font

from pyglet.window import key

from actions import *

import score
import pyglet
import random
import cocos


class Background(Layer):
    def __init__(self):
        super(Background, self).__init__()
        self.img = pyglet.resource.image('media/imgs/background.png')

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

class Game(Scene):

    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()

        score.score_points = 100

        self.load_scenario()
        self.load_catcher()

        self.keys = key.KeyStateHandler()
        director.window.push_handlers(self.keys)

        self.thiefs_builder(1)
        self.schedule_interval(self.thiefs_builder, 10)

    def thiefs_builder(self, dt):
        self.add(FallingThief())

    def load_catcher(self):
        self.catcher = Sprite('media/imgs/catcher.png')
        self.catcher.position = 300,100
        self.catcher.mov_rate = 20
        self.catcher.do( CustomMove(300, 500) )
        self.add(self.catcher)


    def load_scenario(self):
        self.background = Background()
        self.add(self.background)

        self.prison = Sprite('media/imgs/prison.png')
        self.prison.position = 100,170
        self.add(self.prison)

        self.kombi = Sprite('media/imgs/kombi.png')
        self.kombi.position = 790,90
        self.add(self.kombi)

class FallingThief(Layer):

    def __init__(self, *args, **kwargs):
        super(FallingThief, self).__init__()

        thiefs = {'tall': 'media/imgs/tall_thief.png', \
                    'small' : 'media/imgs/small_thief.png', \
                    'fat' : 'media/imgs/fat_thief.png'}
        
        self.thief_type = random.choice(thiefs.items())
        self.thief = Sprite(self.thief_type[1])
        self.thief.alive = True
        self.thief.position = 100, 340
        self.add(self.thief)
        self.fall()

    def fall(self):
        action = CustomJump( self.thief_type[0] )
        self.thief.do(action)

if __name__ == '__main__':
    director.init(resizable=False, width=800, height=600)
    director.run(Game())
