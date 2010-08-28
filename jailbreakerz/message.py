from jailbreakerz import Background
from cocos.director import director

import cocos

class MessageScene(cocos.scene.Scene):
    
    def __init__(self, text):
        super(MessageScene, self).__init__()
        
        self.add(Background())
        
        class UserActivity(cocos.layer.Layer):
            is_event_handler = True
            
            def on_mouse_press(*args):
                director.pop()
                
            def on_text(*args):
                director.pop()
        
        layer = UserActivity()
        self.add(layer)
        
        opts = {
            'font_name': 'against myself',
            'font_size': 70,
            'anchor_x': 'center',
            'anchor_y': 'center',
        }

        label = cocos.text.Label(text, color=(0x00, 0x00, 0x00, 0xff), **opts)
        label.position = 400, 500
        layer.add(label, z=1)

        label = cocos.text.Label(text, color=(0xff, 0xff, 0xff, 0xff), **opts)
        label.position = 400, 503
        layer.add(label, z=2)