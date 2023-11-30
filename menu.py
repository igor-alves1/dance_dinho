from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *

def menu(screen):
    teclado = screen.get_keyboard()
    mouse = screen.get_mouse()
    cursor = Sprite("cursor.png")
    jogar_botao = Animation("bora_dancar3.png", 1)
    jogar_botao.set_position(1*screen.width/24, 13*screen.width/24)
    jogar_botao_grande = Animation("bora_dancar4.png", 1)
    jogar_botao_grande.set_position(jogar_botao.x, jogar_botao.y-(jogar_botao_grande.height-jogar_botao.height)/2)
    venda_botao = Animation("venDINHO3.png", 1)
    venda_botao.set_position(jogar_botao.x, jogar_botao.y+jogar_botao.height)
    venda_botao_grande = Animation("venDINHO4.png", 1)
    venda_botao_grande.set_position(venda_botao.x, venda_botao.y-(venda_botao_grande.height-venda_botao.height)/2)
    select_botao = Animation("playlist3.png", 1)
    select_botao.set_position(jogar_botao.x, venda_botao.y+venda_botao.height)
    select_botao_grande = Animation("playlist4.png", 1)
    select_botao_grande.set_position(select_botao.x, select_botao.y-(select_botao_grande.height-select_botao.height)/2)
    logo = Sprite("logo_dance_dinho2.png")
    logo.set_position(jogar_botao.x, screen.height/24)
    background = GameImage("clouds_background.png")

    dinho = Animation("dinho_walking.png", 4)
    dinho.set_position(screen.width/4, screen.height/2)
    dinho.set_sequence_time(0, 4, 400, True)
    dinho_speed = 120
    
    while True:
        background.draw()
        dinho.play()

        logo.draw()
        if mouse.is_over_area((jogar_botao.x, jogar_botao.y), (jogar_botao.x+jogar_botao.width, jogar_botao.y+jogar_botao.height)):
            jogar_botao_grande.draw()
            if mouse.is_button_pressed(1):
                return 2
        else:
            jogar_botao.draw()
        if mouse.is_over_area((venda_botao.x, venda_botao.y), (venda_botao.x+venda_botao.width, venda_botao.y+venda_botao.height)):
            venda_botao_grande.draw()
        else:
            venda_botao.draw()
        if mouse.is_over_area((select_botao.x, select_botao.y), (select_botao.x+select_botao.width, select_botao.y+select_botao.height)):
            select_botao_grande.draw()
        else:
            select_botao.draw()

        if mouse.is_on_screen():
            mouse.hide()
            coords_mouse = mouse.get_position()
            cursor.set_position(coords_mouse[0], coords_mouse[1])
            cursor.draw()
        else:
            mouse.unhide()

        dinho.draw()
        dinho.x += dinho_speed*screen.delta_time()
        dinho.update()

        screen.update()

    
