from cocos.director import director
from cocos.layer import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
import pyglet

class MainMenu(Menu):

    def __init__(self):
        super( MainMenu, self).__init__('Jail Breakerz') 

        self.font_title['font_size'] = 72
        self.font_item['font_size'] = 32
        self.font_item_selected['font_size'] = 46

        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append(MenuItem('New Game', self.new_game))
        items.append(MenuItem('Quit', self.quit))

        self.create_menu(items)

    def quit(self):
        pyglet.app.exit()
    
    def new_game(self):
        pass

if __name__ == "__main__":

    director.init(resizable=True, width=600, height=720)
    scene = Scene()
    scene.add(MainMenu()) 

    director.run(scene)
