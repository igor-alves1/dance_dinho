from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *

def select(screen):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    cursor = Sprite("assets/cursor.png")
    background = GameImage("assets/clouds_background.png")

    twinkle = Sprite("assets/twinkle_button.png")
    twinkle.set_position((screen.width-twinkle.width)/2, screen.height/4)
    twinkle_hover = Sprite("assets/twinkle_button_hover.png")
    twinkle_hover.set_position(twinkle.x, twinkle.y)

    fase3 = Sprite("assets/rockabye_button.png")
    fase3.set_position(twinkle.x, twinkle.y+twinkle.height)
    rockabye_hover = Sprite("assets/rockabye_button_hover.png")
    rockabye_hover.set_position(fase3.x, fase3.y)

    mars = Sprite("assets/to_mars_button.png")
    mars.set_position(twinkle.x, fase3.y+fase3.height)
    mars_hover = Sprite("assets/to_mars_button_hover.png")
    mars_hover.set_position(mars.x, mars.y)

    seta = Sprite("assets/seta_voltar.png")
    seta.set_position(screen.width*0.01, screen.height*0.01)
    seta_grande = Sprite("assets/seta_voltar_grande.png")
    seta_grande.set_position(seta.x, seta.y)

    celular = Sprite("assets/celular7.png")
    celular.set_position(twinkle.x-(celular.width-twinkle.width), twinkle.y-25)

    while True:
        coords = mouse.get_position()
        cursor.set_position(coords[0], coords[1])
        screen.update()
        background.draw()
        if mouse.is_over_object(twinkle):
            twinkle_hover.draw()
            screen.draw_text("00000", x=twinkle.x+35, y=twinkle.y+7*twinkle.height/10, color=(255,255,255), size=12)
        else:
            twinkle.draw()
        if mouse.is_over_object(fase3):
            rockabye_hover.draw()
            screen.draw_text("00000", x=fase3.x+35, y=fase3.y+7*fase3.height/10, color=(255,255,255), size=12)
        else:
            fase3.draw()
        if mouse.is_over_object(mars):
            mars_hover.draw()
            screen.draw_text("00000", x=mars.x+35, y=mars.y+7*mars.height/10, color=(255,255,255), size=12)
        else:
            mars.draw()
        celular.draw()

        if mouse.is_over_object(seta):
            seta_grande.draw()
            if mouse.is_button_pressed(1):
                return 1
        else:
            seta.draw()
        if mouse.is_over_object(twinkle) and mouse.is_button_pressed(1):
            doc = open("curr_phase.txt", 'w')
            doc.write("twinkle")
            doc.close()
            return 2
        if mouse.is_over_object(mars) and mouse.is_button_pressed(1):
            doc = open("curr_phase.txt", "w")
            doc.write("mars")
            doc.close()
            return 2
        cursor.draw()
        
