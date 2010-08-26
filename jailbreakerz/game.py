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

from actions import *

import score
import pyglet
import random
import cocos

class Game(Layer):

    def __init__(self):
        super(Game, self).__init__()
        self.load_sprites()
        
        score.score_points = 100
        
        # THIEF BUILDER
        # TODO : And how we gonna do in hard levels?
        self.schedule_interval(self.thief_builder, 2)

    def thief_builder(self, dt):
        self.add(FallingThief())

    def load_sprites(self):
        self.prison = Sprite('media/imgs/prison.png')
        self.prison.position = 100,170
        self.add(self.prison)

        self.kombi = Sprite('media/imgs/kombi.png')
        self.kombi.position = 790,90
        self.add(self.kombi)


class FallingThief(Layer):

    def __init__(self, *args, **kwargs):
        super(FallingThief, self).__init__()

        thief_sprites = ['media/imgs/tall_thief.png', 'media/imgs/small_thief.png', 'media/imgs/fat_thief.png']
        self.thief = Sprite(random.sample(thief_sprites, 1)[0])
        self.thief.position = 100, 190
        self.add(self.thief)
        self.fall()

    def fall(self):
        action = CustomJump((500,0), 100, 10, 7)
        self.thief.do(action)
        pyglet.resource.media('media/sounds/yupi.mp3').play()


class Catcher(Layer):
 
    is_event_handler = True

    MOVEMENT_RATE = 100  # Constant used to move sprite

    def __init__(self, *args, **kwargs):
        super(Catcher, self).__init__()
        self.catcher = Sprite('media/imgs/catcher.png')
        self.catcher.position = 300,100
        self.add(self.catcher)

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.LEFT and self.catcher.position[0] > 300:
            self.catcher.position = self.catcher.position[0] - self.MOVEMENT_RATE, self.catcher.position[1]
        elif key == pyglet.window.key.RIGHT and self.catcher.position[0] < 500:
            self.catcher.position = self.catcher.position[0] + self.MOVEMENT_RATE, self.catcher.position[1]

if __name__ == '__main__':
    director.init(resizable=False, width=800, height=600)
    scene = Scene(Game(), Catcher(), FallingThief() )
    director.run(scene)
