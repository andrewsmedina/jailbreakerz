import os

from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
from pyglet import font

from score import ScoreLayer

import pyglet

import sound
import credits
import game

class Background(Layer):
    def __init__(self):
        super(Background, self).__init__()
        self.img = pyglet.resource.image('media/imgs/wall_bg_dark.jpg')

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

class Shadow(Layer):
    def __init__(self):
        super(Shadow, self).__init__()
        label = Label('Jailbreakerz',
            font_name='against myself',
            font_size=70,
            anchor_x='center', anchor_y='center',
            color=(0, 0, 0, 200)
        )
        label.position = 400, 497
        self.add(label)

        label = Label('Start',
            font_name='against myself',
            font_size=46,
            anchor_x='center', anchor_y='center',
            color=(0, 0, 0, 200)
        )
        label.position = 400, 188
        self.add(label)

        label = Label('Credits',
            font_name='against myself',
            font_size=46,
            anchor_x='center', anchor_y='center',
            color=(0, 0, 0, 200)
        )
        label.position = 400, 125
        self.add(label)

        label = Label('Quit',
            font_name='against myself',
            font_size=46,
            anchor_x='center', anchor_y='center',
            color=(0, 0, 0, 200)
        )
        label.position = 400, 62
        self.add(label)


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Jailbreakerz')

        self.font_title['font_size'] = 70
        self.font_title['font_name'] = "against myself"
        self.font_title['color'] = (255, 255, 255, 255)
        self.font_title['anchor_y'] = "top"

        self.font_item['font_size'] = 46
        self.font_item['font_name'] = "against myself"
        self.font_item['color'] = (0xf6, 0xef, 0x8f, 255) #F6DF8F

        self.font_item_selected['font_size'] = 50
        self.font_item_selected['font_name'] = "against myself"
        self.font_item_selected['color'] = (255, 255, 255, 255)

        self.menu_valign = BOTTOM

        items = []

        items.append(MenuItem('Start', self.on_start))
        items.append(MenuItem('Credits', self.on_credits))
        items.append(MenuItem('Quit', self.on_quit))

        self.create_menu(items)

        sound.player.queue(pyglet.resource.media('media/sounds/fundogame.mp3'))
        sound.player.eos_action = 'loop'
        sound.player.play()

    def on_start(self):
        game_scene = game.Game()
        game_scene.add(ScoreLayer(), z=2)
        director.push( game_scene  )

    def on_credits(self):
        scene = Scene(Background())
        scene.add(credits.Credits())
        director.push(scene)

    def on_quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    font_path = os.path.join( os.path.dirname(__file__), 'media/font')
    font.add_directory(font_path)

    director.init(resizable=False, width=800, height=600)

    scene = Scene(Background())
    scene.add(MainMenu(), z=2)
    scene.add(Shadow(), z=1)

    director.run(scene)

