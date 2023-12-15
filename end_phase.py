from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

def end_phase(screen, score, necessario):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    background = GameImage("assets/clouds_background.png")
    try_again = Sprite("assets/repetir.png")
    try_again.set_position((screen.width-(try_again.width/2))/4, screen.height/2)
    try_again_grande = Sprite("assets/repetir_grande.png")
    try_again_grande.set_position(try_again.x, try_again.y)
    back = Sprite("assets/seta_voltar.png")
    back.set_position(3*(screen.width-(back.width/2))/4, screen.height/2)
    back_grande = Sprite("assets/seta_voltar_grande.png")
    back_grande.set_position(back.x, back.y)

    if score > necessario:
        doc = open("coins.txt", 'r')
        coins = int(doc.readline())
        doc.close()
        doc = open("coins.txt", 'w')
        coins += 5
        doc.write(str(coins))
        doc.close()

    cursor = Sprite("assets/cursor.png")
    
    while True:
        screen.update()
        background.draw()
        coords = mouse.get_position()
        cursor.set_position(coords[0], coords[1])

        if (score > necessario):
            screen.draw_text(f'Parabéns!', x=screen.width/3-40,
                             y=40, color=(49,12,92),
                             size=20, bold=True)
            screen.draw_text(f'Você marcou {score} pontos e ganhou 5 moedas!', x=screen.width/3-40,
                             y=80, color=(49,12,92), size=14, bold=True)
        else:
            screen.draw_text(f'Boa tentativa...', x=screen.width/4-40,
                             y=40, color=(49,12,92), bold=True)
            screen.draw_text("Mas você não conseguiu atingir a pontuação mínima para passar de fase...", x=screen.width/4-40,
                             y=80, color=(49,12,92), bold=True)

        if mouse.is_over_object(back):
            back_grande.draw()
            if mouse.is_button_pressed(1):
                return 1
        else:
            back.draw()
        if mouse.is_over_object(try_again):
            try_again_grande.draw()
            if mouse.is_button_pressed(1):
                return 2
        else:
            try_again.draw()
        cursor.draw()
        
        
