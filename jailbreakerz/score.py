from cocos.layer import *
from cocos.text import *
from cocos.actions import *

import pyglet
from pyglet.gl import *

score_points = 0

class ScoreLayer(Layer): 
    def __init__(self):
        super(ScoreLayer, self).__init__()

        self.score = Label('score:', 
                           font_size=12,
                           color=(255,255,255,255))
        
        self.position = (700, 580)                   
        self.score.position = (0,0)
        self.add(self.score)

    def draw(self):
        super(ScoreLayer, self).draw()
        self.score.element.text = 'Score: %d' % score_points
