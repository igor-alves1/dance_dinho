from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.sound import *

def shop(screen):
    keyboard = screen.get_keyboard()
    mouse = screen.get_mouse()
    background = GameImage("assets/clouds_background.png")
    chao = GameImage("assets/chao_loja.png")
    dinho = Animation("assets/dinho_walking.png", 4)
    dinho.set_position(-dinho.width, screen.height/2)
    dinho.set_sequence_time(0, 4, 400, True)
    dinho_speed = 120
    chao.set_position(0, dinho.y + 9*dinho.height/10)
    tenda = GameImage("assets/vendinha_dinho.png")
    tenda.set_position(3*screen.width/4-tenda.width/2, chao.y-tenda.height)
    itens = []
    contador_itens = 0
    guaravita = Animation("assets/guaramor_formato.png", 2)
    guaravita.set_position(tenda.x+tenda.width/4+5, tenda.y+tenda.height/2-11)
    itens.append(guaravita)
    burger = Animation("assets/burger_formato.png", 2)
    burger.set_position(guaravita.x+12, guaravita.y+(guaravita.height-burger.height))
    itens.append(burger)
    itens[contador_itens].set_curr_frame(1)
    seta_tick = 0.15
    timer_aperto = 0

    while True:
        screen.update()
        dinho.update()
        timer_aperto += screen.delta_time()
        background.draw()
        chao.draw()
        for item in itens:
            item.draw()
        tenda.draw()
        itens[contador_itens%len(itens)].draw()
        dinho.draw()
        if dinho.x >= 3*screen.width/4:
            dinho.x = 3*screen.width/4 - 1
            dinho_speed = 0
            dinho.stop()
        else:
            dinho.x += dinho_speed*screen.delta_time()

        if dinho.is_playing():
            continue

        if keyboard.key_pressed('right') and timer_aperto > seta_tick:
            itens[abs(contador_itens)%len(itens)].set_curr_frame(0)
            contador_itens += 1
            itens[abs(contador_itens)%len(itens)].set_curr_frame(1)
            timer_aperto = 0
        elif keyboard.key_pressed('left') and timer_aperto > seta_tick:
            itens[abs(contador_itens)%len(itens)].set_curr_frame(0)
            contador_itens -= 1
            itens[abs(contador_itens)%len(itens)].set_curr_frame(1)
            timer_aperto = 0

        if keyboard.key_pressed('esc'):
            return 1
        
