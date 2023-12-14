from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *

def select(screen):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    cursor = Sprite("assets/cursor.png")
    background = GameImage("assets/fundo_playlist.png")
    
    playlist = GameImage("assets/playlist_titulo.png")
    playlist.set_position(screen.width*0.18, screen.height*0.09)

    twinkle = Sprite("assets/exemplofase1.png")
    twinkle.set_position(screen.width*0.18, screen.height*0.393)

    fase2 = Sprite("assets/exemplofase2.png")
    fase2.set_position(screen.width*0.606, screen.height*0.393)

    fase3 = Sprite("assets/exemplofase3.png")
    fase3.set_position(screen.width*0.18, screen.height*0.606)

    mars = Sprite("assets/exemplofase4.png")
    mars.set_position(screen.width*0.606, screen.height*0.606)

    seta = Sprite("assets/voltar1.png")
    seta.set_position(screen.width*0.01, screen.height*0.01)    

    while True:
        coords = mouse.get_position()
        cursor.set_position(coords[0], coords[1])
        screen.update()
        background.draw()
        twinkle.draw()
        fase2.draw()
        fase3.draw()
        mars.draw()
        seta.draw()
        cursor.draw()

        if mouse.is_over_object(seta) and mouse.is_button_pressed(1):
            return 1
        elif mouse.is_over_object(twinkle) and mouse.is_button_pressed(1):
            doc = open("curr_phase.txt", 'w')
            doc.write("twinkle")
            doc.close()
            return 2
        elif mouse.is_over_object(mars) and mouse.is_button_pressed(1):
            doc = open("curr_phase.txt", "w")
            doc.write("mars")
            doc.close()
            return 2
        
