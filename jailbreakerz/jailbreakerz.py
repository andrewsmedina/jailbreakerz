from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
import pyglet

class Background(Layer):
    def __init__(self):
        super(Background, self).__init__()
        self.img = pyglet.resource.image('media/imgs/wall_bg.jpg')

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()


class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__('Jailbreakerz')

        self.font_title['font_size'] = 70
        self.font_title['font_name'] = "against myself"
        self.font_title['color'] = (0, 0, 0, 255)
        self.font_title['anchor_y'] = "top"

        self.font_item['font_size'] = 46
        self.font_item['font_name'] = "against myself"
        self.font_item['color'] = (0, 0, 0, 200) #190C02

        self.font_item_selected['font_size'] = 46
        self.font_item_selected['font_name'] = "against myself"
        self.font_item_selected['color'] = (255, 255, 255, 200) #F8FDCE

        self.menu_valign = BOTTOM

        items = []

        items.append(MenuItem('START', self.on_start))
        items.append(MenuItem('CREDITS', self.on_credits))
        items.append(MenuItem('QUIT', self.on_quit))

        self.create_menu(items)

    def on_start(self):
        pass

    def on_credits(self):
        pass

    def on_quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    director.init(resizable=False, width=800, height=600)

    scene = Scene(Background())
    scene.add(MainMenu())

    director.run(scene)

