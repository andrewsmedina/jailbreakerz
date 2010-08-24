import random
import cocos
import pyglet

class Game(cocos.layer.Layer):

    def __init__(self):
        super(Game, self).__init__()
        self.load_sprites()

    def load_sprites(self):
        self.prison = cocos.sprite.Sprite('media/imgs/prison.png')
        self.prison.position = 100,170
        self.add(self.prison)

        self.kombi = cocos.sprite.Sprite('media/imgs/kombi.png')
        self.kombi.position = 750, 120
        self.add(self.kombi)

class Catcher(cocos.layer.Layer):
    
    is_event_handler = True
    
    MOVEMENT_RATE = 100  # Constant used to move sprite
    
    def __init__(self, *args, **kwargs):
        super(Catcher, self).__init__()
        self.catcher = cocos.sprite.Sprite('media/imgs/catcher.png')
        self.catcher.position = 300,100
        self.add(self.catcher)
        
    def on_key_press(self, key, modifiers):
        """
        Catcher movement
        
        @param key: int
        """
        if key == pyglet.window.key.LEFT:
            self.catcher.position = self.catcher.position[0] - self.MOVEMENT_RATE, self.catcher.position[1]
        elif key == pyglet.window.key.RIGHT:
            self.catcher.position = self.catcher.position[0] + self.MOVEMENT_RATE, self.catcher.position[1]            


class Thief(cocos.layer.Layer):
    """
    Thief that flies.
    """
    def __init__(self, *args, **kwargs):
        super(Thief, self).__init__()
        thief_sprites = ['media/imgs/tall_thief.png', 'media/imgs/small_thief.png', 'media/imgs/fat_thief.png']
        self.thief = cocos.sprite.Sprite(random.sample(thief_sprites, 1)[0])  # Create a random thief
        self.thief.position = 250,440
        self.add(self.thief)

if __name__ == '__main__':
    cocos.director.director.init(resizable=False, width=800, height=600)
    # XXX THIS CODE IS NOT BEING USED
    scene = cocos.scene.Scene(Game(), Catcher(), Thief())
    cocos.director.director.run(scene)
