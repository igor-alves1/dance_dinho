from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *


def select(screen):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    background = GameImage("assets/fundo_playlist.png")
    
    playlist = GameImage("assets/playlist_titulo.png")
    playlist.set_position(screen.width*0.18, screen.height*0.09)

    twinkle = GameImage("assets/exemplofase1.png")
    twinkle.set_position(screen.width*0.18, screen.height*0.393)

    fase2 = GameImage("assets/exemplofase2.png")
    fase2.set_position(screen.width*0.606, screen.height*0.393)

    fase3 = GameImage("assets/exemplofase3.png")
    fase3.set_position(screen.width*0.18, screen.height*0.606)

    fase4 = GameImage("assets/exemplofase4.png")
    fase4.set_position(screen.width*0.606, screen.height*0.606)

    seta = GameImage("assets/voltar1.png")
    seta.set_position(screen.width*0.01, screen.height*0.01)    

    while True:
        screen.update()
        background.draw()
        twinkle.draw()
        fase2.draw()
        fase3.draw()
        fase4.draw()
        seta.draw()

        if  mouse.is_over_area((seta.x, seta.y), (seta.x+seta.width, seta.y+seta.height)):
            if mouse.is_button_pressed(1):
                return 1         
