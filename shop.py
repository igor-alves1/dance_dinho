from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *

def shop(screen):
    background = GameImage("clouds_background.png")
    chao = GameImage("chao_loja.png")
    dinho = Animation("dinho_walking.png", 4)
    dinho.set_position(-dinho.width, screen.height/2)
    dinho.set_sequence_time(0, 4, 400, True)
    dinho_speed = 120
    chao.set_position(0, dinho.y + 9*dinho.height/10)
    tenda = GameImage("vendinha_dinho.png")
    tenda.set_position(3*screen.width/4-tenda.width/2, chao.y-tenda.height)
    

    while True:
        background.draw()
        chao.draw()
        tenda.draw()
        dinho.draw()
        if dinho.x >= 3*screen.width/4:
            dinho.x = 3*screen.width/4 - 1
            dinho_speed = 0
            dinho.stop()
        else:
            dinho.x += dinho_speed*screen.delta_time()

        screen.update()
        dinho.update()
        
