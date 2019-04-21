
import cocos
from cocos.scenes.transitions import FadeTransition
import pyglet
import collections
from pyglet.window import key
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.euclid import Vector2
from collections import defaultdict

class VerTexto(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        mi_etiqueta = cocos.text.Label('Gladiator', font_name ='Consolas', font_size = 22,
                                       anchor_x = 'center', anchor_y = 'center')
        mi_etiqueta.position = (320,240)
        self.add(mi_etiqueta)

class VerTexto2(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        mi_etiqueta = cocos.text.Label('Roma 980 AC...', font_name ='Consolas', font_size = 22,
                                       anchor_x = 'center', anchor_y = 'center')
        mi_etiqueta.position = (320,240)
        self.add(mi_etiqueta)



if __name__ == '__main__':
    cocos.director.director.init(caption='Gladiator')

    escena_1 = cocos.scene.Scene(VerTexto())
    escena_2 = cocos.scene.Scene(VerTexto2())

    cocos.director.director.run(FadeTransition(escena_2, 5, escena_1))