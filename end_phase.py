from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

def end_phase(screen, score):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    background = GameImage("assets/clouds_background.png")
    try_again = Sprite("assets/exemplofase1.png")
    try_again.set_position((screen.width-(try_again.width/2))/4, screen.height/2)
    menu = Sprite("assets/exemplofase2.png")
    menu.set_position(3*(screen.width-(menu.width/2))/4, screen.height/2)

    if score > 3500:
        doc = open("coins.txt", 'r')
        coins = int(doc.readline())
        doc.close()
        doc = open("coins.txt", 'w')
        coins += 30
        doc.write(str(coins))
        doc.close()

    cursor = Sprite("assets/cursor.png")
    
    while True:
        screen.update()
        background.draw()
        coords = mouse.get_position()
        cursor.set_position(coords[0], coords[1])

        if (score > 3500):
            screen.draw_text(f'Parabéns!', x=screen.width/3-40,
                             y=40, color=(49,12,92),
                             size=20, font_name="ocr-a", bold=True)
            screen.draw_text(f'Você marcou {score} pontos e ganhou 30 moedas!', x=screen.width/3-40,
                             y=60, color=(49,12,92),
                             size=20, font_name="ocr-a", bold=True)
        else:
            screen.draw_text(f'Boa tentativa, mas você não conseguiu atingir a pontuação mínima para passar de fase...', x=screen.width/4-40,
                             y=40, color=(49,12,92),
                             size=20, font_name="ocr-a", bold=True)

        try_again.draw()
        menu.draw()
        if mouse.is_over_object(menu) and mouse.is_button_pressed(1):
            return 1
        if mouse.is_over_object(try_again) and mouse.is_button_pressed(1):
            return 2
        cursor.draw()
        
        
