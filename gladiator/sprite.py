import cocos
import bezier
import numpy as np

from cocos.actions import *

class MisAcciones(cocos.layer.ColorLayer):
    def __init__(self):
        super().__init__(64,200,255,255)

        mi_sprite = cocos.sprite.Sprite('Rostro1.gif')
        mi_sprite.position = 320 , 240
        mi_sprite.scale = 0.05
        self.add(mi_sprite)

        escalar1 = ScaleBy(3, duration = 2)
        salto = JumpTo((100,100),10,5,6)

        curve = nodes = np.asfortranarray([
             [0.0, 0.625, 1.0],
             [0.0, 0.5, 0.5],
             ])
        curve = bezier.Curve(nodes, degree=2)



        mi_sprite.do(escalar1 + Reverse(escalar1))
        mi_sprite.do(salto)
        mi_sprite.do(curve)



if __name__ == "__main__":
    cocos.director.director.init(caption='Sprite de Gladiator')
    mi_capa = MisAcciones()
    mi_escena = cocos.scene.Scene(mi_capa)
    cocos.director.director.run(mi_escena)