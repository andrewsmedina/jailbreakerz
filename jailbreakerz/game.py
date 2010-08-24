import cocos


class Game(cocos.layer.Layer):

    def __init__(self):
        super(Game, self).__init__()
        self.load_sprites()

    def load_sprites(self):
        self.prison = cocos.sprite.Sprite('media/imgs/prison.png')
        self.prison.position = 100,170
        self.add(self.prison)

        self.thief = cocos.sprite.Sprite('media/imgs/tall_thief.png')
        self.thief.position = 250,440
        self.add(self.thief)

        self.catcher = cocos.sprite.Sprite('media/imgs/catcher.png')
        self.catcher.position = 300,100
        self.add(self.catcher)

        self.kombi = cocos.sprite.Sprite('media/imgs/kombi.png')
        self.kombi.position = 750, 120
        self.add(self.kombi)

if __name__ == '__main__':
    cocos.director.director.init(resizable=False, width=800, height=600)

    scene = cocos.scene.Scene(Game())
    cocos.director.director.run(scene)
