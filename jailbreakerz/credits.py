import cocos

class Credits(cocos.layer.Layer):

    def __init__(self):
        super(Credits, self).__init__()
        
        label = cocos.text.Label('Credits',
                                  font_name='against myself',
                                  font_size=70,
                                  anchor_x='center', 
                                  anchor_y='center',
                                  color=(0, 0, 0, 255))
        
        label.position = 400,510
   
        self.add(label)

if __name__ == '__main__':
    cocos.director.director.init(resizable=False, width=800, height=600)

    scene = cocos.scene.Scene(Credits())
    cocos.director.director.run(scene)
