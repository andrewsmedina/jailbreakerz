# -*- encoding: utf-8 -*-

import cocos

from cocos.layer import Layer
from cocos.text import Label, HTMLLabel


DEVELOPERS = u"""
<center>
<font size="+1" color="white" face="Arial"><b>Developers</b></font>
<br><font color="white" face="Arial">Andrews Medina <tt>&lt;andrewsmedina@gmail.com&gt;</tt></font>
<br><font color="white" face="Arial">Bernardo Heynemann <tt>&lt;heynemann@gmail.com&gt;</tt></font>
<br><font color="white" face="Arial">Diógenes <tt>&lt;diofeher@gmail.com&gt;</tt></font>
<br><font color="white" face="Arial">Enrico Batista da Luz <tt>&lt;ricobl@gmail.com&gt;</tt></font>
<br><font color="white" face="Arial">Flávio Ribeiro <tt>&lt;email@flavioribeiro.com&gt;</tt></font>
<br><font color="white" face="Arial">Igor Sobreira <tt>&lt;igor@igorsobreira.com&gt;</tt></font>
<br><font color="white" face="Arial">Osvaldo Santana Neto <tt>&lt;osantana@gmail.com&gt;</tt></font>
<p>
<font size="+1" color="white" face="Arial"><b>Background</b></font><br>
<font color="white" face="Arial">Ashour Rehana <tt>http://flickr.com/photos/arehana</tt></font>
</p>
</center>
"""


class Credits(Layer):
    def __init__(self):
        super(Credits, self).__init__()

        opts = {
            'font_name': 'against myself',
            'font_size': 70,
            'anchor_x': 'center',
            'anchor_y': 'center',
        }

        label = Label('Credits', color=(0x00, 0x00, 0x00, 0xff), **opts)
        label.position = 400, 500
        self.add(label, z=1)

        label = Label('Credits', color=(0xff, 0xff, 0xff, 0xff), **opts)
        label.position = 400, 503
        self.add(label, z=2)

        shadow = DEVELOPERS.replace("white", "black")
        developers = HTMLLabel(shadow, width=760, height=300, multiline=True)
        developers.position = 20, 298
        self.add(developers, z=1)

        developers = HTMLLabel(DEVELOPERS, width=760, height=300, multiline=True)
        developers.position = 20, 300
        self.add(developers, z=2)



if __name__ == '__main__':
    cocos.director.director.init(resizable=False, width=800, height=600)
    scene = cocos.scene.Scene(Credits())
    cocos.director.director.run(scene)
