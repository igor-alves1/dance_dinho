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
    cifra = Sprite("assets/cifra.png")
    cifra.set_position(screen.width/16, screen.height/16)

    doc = open("coins.txt", 'r')
    coins = int(doc.readline())
    doc.close()
    
    itens = []
    contador_itens = 0
    
    guaravita = Animation("assets/guaramor_formato.png", 2)
    guaravita.set_position(tenda.x+tenda.width/4+15, tenda.y+tenda.height/2-11)
    itens.append(guaravita)
    
    burger = Animation("assets/burger_formato.png", 2)
    burger.set_position(guaravita.x+guaravita.width+10, guaravita.y+(guaravita.height-burger.height))
    itens.append(burger)

    jordan1 = Animation("assets/jordan1.png", 2)
    jordan1.set_position(burger.x+burger.width+10, guaravita.y+(guaravita.height-jordan1.height)+20)
    itens.append(jordan1)
    
    itens[contador_itens].set_curr_frame(1)
    seta_tick = 0.15
    timer_aperto = 0

    preco = 25
    item_flag = False

    #cenario
    lamp_post1 = Sprite("assets/lamp_post.png")
    lamp_post1.set_position(screen.width/32, chao.y-lamp_post1.height+6)
    tenda1 = Sprite("assets/tenda_cenario1.png")
    tenda1.set_position(lamp_post1.x+lamp_post1.width/2, tenda.y)
    lixeira = Sprite("assets/trashcan.png")
    lixeira.set_position(tenda1.x+tenda1.width+lixeira.width/4, chao.y-lixeira.height+10)
    lamp_post2 = Sprite("assets/lamp_post.png")
    lamp_post2.set_position(lixeira.x-lixeira.width/2, lamp_post1.y)

    esc_timer = 0
    esc_tick = 1
    print_esc = True

    back = Sprite("assets/seta_voltar.png")
    back.set_position(screen.width/16, 14*screen.height/16)
    back_grande = Sprite("assets/seta_voltar_grande.png")
    back_grande.set_position(back.x, back.y)

    cursor = Sprite("assets/cursor.png")
    
    while True:
        screen.update()
        dinho.update()
        coords = mouse.get_position()
        cursor.set_position(coords[0], coords[1])
        timer_aperto += screen.delta_time()
        background.draw()
        chao.draw()
        tenda1.draw()
        lamp_post1.draw()
        tenda.draw()
        lixeira.draw()
        lamp_post2.draw()
        cifra.draw()
        for item in itens:
            item.draw()
        itens[contador_itens%len(itens)].draw()
        dinho.draw()
        if mouse.is_over_object(back):
            back_grande.draw()
            if mouse.is_button_pressed(1):
                return 1
        else:
            back.draw()

        screen.draw_text(f'{coins}', x=cifra.x+cifra.width, y=cifra.y+cifra.height/3, size=25,
                         font_name="ocr-a", color=(49, 12, 92) , bold=True)
        
        if dinho.x >= 3*screen.width/4 and not item_flag:
            dinho.x = 3*screen.width/4 - 1
            dinho_speed = 0
            dinho.stop()
        elif dinho.x >= screen.width:
            return 0
        else:
            dinho.x += dinho_speed*screen.delta_time()

        if dinho.is_playing():
            continue

        screen.draw_text("Deseja comprar algo para ajudá-lo na próxima fase?",
                         x=screen.width/4-20, y=screen.height/6, size=14, color=(49,12,92), bold = True)
        if item_flag == False:
            if esc_timer < esc_tick:
                esc_timer += screen.delta_time()
            else:
                esc_timer = 0
                print_esc = abs(print_esc-1)
            if print_esc:
                screen.draw_text("(caso não queira, pressione ESC para avançar)", x=screen.width/4,
                                 y=screen.height/4, size=14, color=(49,12,92))
        
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

        if keyboard.key_pressed('enter') and coins > preco:
            power_up = open("powerups.txt", 'w')
            power_up.write(str(abs(contador_itens)%len(itens)))
            power_up.close()
            doc = open("coins.txt", 'w')
            coins -= 25
            doc.write(str(coins))
            doc.close()
            dinho.play()
            dinho_speed = 120
            item_flag = True
        elif keyboard.key_pressed('enter') and coins < preco:
            pass

        if keyboard.key_pressed('esc'):
            item_flag = True
            dinho_speed = 120
            dinho.play()
        cursor.draw()
        
