from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

def readToList(doc_name, array):
    file = open(doc_name, 'r')
    for line in file:
        value = line.strip()
        time = float(value[:6])
        array.append(time)
    file.close()

def judge_inputs(key_entered, arrows_array, super_bar, checker_right, xplosion_list):
    if len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<5:
        seta = arrows_array.pop(0)
        new_xplosion = Animation("assets/xplosion_spritesheet.png", 6)
        new_xplosion.set_sequence_time(0, 5, 100, loop=False)
        new_xplosion.set_position(seta.x, seta.y)
        new_xplosion.play()
        xplosion_list.append(new_xplosion)
        super_bar.height += 5
        return "perfect"
    elif len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<15:
        seta = arrows_array.pop(0)
        new_xplosion = Animation("assets/xplosion_spritesheet.png", 6)
        new_xplosion.set_sequence_time(0, 5, 100, loop=False)
        new_xplosion.set_position(seta.x, seta.y)
        new_xplosion.play()
        xplosion_list.append(new_xplosion)
        return "good"
    elif len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<25:
        seta = arrows_array.pop(0)
        new_xplosion = Animation("assets/xplosion_spritesheet.png", 6)
        new_xplosion.set_sequence_time(0, 5, 100, loop=False)
        new_xplosion.set_position(seta.x, seta.y)
        new_xplosion.play()
        xplosion_list.append(new_xplosion)
        return "ok"
    elif len(arrows_array)>0:
        seta = arrows_array.pop(0)
        new_xplosion = Animation("assets/xplosion_spritesheet.png", 6)
        new_xplosion.set_sequence_time(0, 5, 100, loop=False)
        new_xplosion.set_position(seta.x, seta.y)
        new_xplosion.play()
        xplosion_list.append(new_xplosion)
        super_bar.height = 0
        return "miss"
    else:
        return "miss"

def judge_resposta(resposta):
    if resposta == "perfect":
        return 50
    elif resposta == "good":
        return 20
    elif resposta == "ok":
        return 10
    return -30

def special_use(moving_arrows_array, xplosion_list):
    score_special = 50
    while len(moving_arrows_array)>0:
        seta = moving_arrows_array.pop(0)
        new_xplosion = Animation("assets/xplosion_spritesheet.png", 6)
        new_xplosion.set_sequence_time(0, 5, 100, loop=False)
        new_xplosion.set_position(seta.x, seta.y)
        new_xplosion.play()
        xplosion_list.append(new_xplosion)
        score_special += 50

    return score_special

def phase(screen, music):
    keyboard = screen.get_keyboard()
    background = GameImage("assets/clouds_background.png")

    dinho = Animation("assets/dinho_walking.png", 4)
    dinho.set_position(-dinho.width, screen.height/2)
    dinho.set_sequence_time(0, 4, 400, True)
    dinho_speed = 120
    chao = GameImage("assets/chao_loja.png")
    chao.set_position(0, dinho.y + 9*dinho.height/10)

    up_list, down_list, right_list, left_list = [], [], [], []
    song = Sound(f"docs/{music}/{music}.ogg")
    readToList(f'docs/{music}/{music}_up_file.txt', up_list)
    readToList(f'docs/{music}/{music}_down_file.txt', down_list)
    readToList(f'docs/{music}/{music}_left_file.txt', left_list)
    readToList(f'docs/{music}/{music}_right_file.txt', right_list)

    arrows_speed = 140
    arrow_tick = 0
    up_i, down_i, left_i, right_i = 0, 0, 0, 0

    timer = 0
    countdown = 3
    enter_pressed = False

    moving_arrows_up, moving_arrows_down, moving_arrows_left, moving_arrows_right = [], [], [], []
    music_is_on = False

    checker_right = Sprite("assets/checker_right.png")
    checker_right.set_position(14*screen.width/16, 14*screen.height/16)
    checker_up = Sprite("assets/checker_up.png")
    checker_up.set_position(14*screen.width/16, 11*screen.height/16)
    checker_down = Sprite("assets/checker_down.png")
    checker_down.set_position(14*screen.width/16, 12*screen.height/16)
    checker_left = Sprite("assets/checker_left.png")
    checker_left.set_position(14*screen.width/16, 13*screen.height/16)
    fx_right = Sprite("assets/shining_left.png")
    fx_right.set_position(checker_right.x, checker_right.y)
    fx_up = Sprite("assets/shining_up.png")
    fx_up.set_position(checker_up.x, checker_up.y)
    fx_left = Sprite("assets/shining_right.png")
    fx_left.set_position(checker_left.x, checker_left.y)
    fx_down = Sprite("assets/shining_down.png")
    fx_down.set_position(checker_down.x, checker_down.y)

    image_meter = GameImage("assets/fix_meter.png")
    image_meter.set_position(14*screen.width/16, 2*(screen.height-image_meter.height)/6)
    super_meter = Sprite("assets/meter.png")
    super_meter.set_position(image_meter.x, image_meter.y)
    super_meter.height = 0

    resposta = ""

    score = 0
    score_hud = Sprite("assets/score_hud.png")
    score_hud.set_position(screen.width/32, score_hud.height)
    time_hud = Sprite("assets/timer_hud.png")
    time_hud.set_position(score_hud.x, score_hud.y+score_hud.height)

    xplosion_list = []

    while True:
        screen.update()
        dinho.update()
        background.draw()
        chao.draw()
        score_hud.draw()
        time_hud.draw()
        dinho.draw()
        if dinho.x >= 3*screen.width/4:
            dinho.x = 3*screen.width/4 - 1
            dinho_speed = 0
            dinho.stop()
        else:
            dinho.x += dinho_speed*screen.delta_time()

        if dinho.is_playing():
            continue
        
        checker_right.draw()
        checker_left.draw()
        checker_up.draw()
        checker_down.draw()
        image_meter.draw()
        super_meter.draw()

        #inicia o countdown quando é apertada a tecla enter
        if keyboard.key_pressed('enter'):
            enter_pressed = True
        if countdown > 0 and enter_pressed:
            countdown -= screen.delta_time()
            screen.draw_text(f'{countdown:.0f}', screen.width/2, screen.height/8, color=(16,22,51), size=20)

        if countdown <= 0 and music_is_on==False:
            song.play()
            music_is_on = True
            enter_pressed = False
                
        #inicia o timer e exibe o timer e o score na tela
        if music_is_on:
            timer += screen.delta_time()
            screen.draw_text(f'{timer:.0f}', time_hud.x+score_hud.width, time_hud.y, color=(49,12,92), size=20, font_name="ocr-a", bold=True)
            screen.draw_text(f'{score}', score_hud.x+score_hud.width, score_hud.y, color=(49,12,92), size=20, font_name="ocr-a", bold=True)
            screen.draw_text(f'{resposta}', checker_up.x, checker_up.y-40, color=(171,27,196), size=15, font_name="ocr-a", bold=True)

        #faz as setinhas surgirem com delay para chegarem do outro lado na tela no tempo certo
        if len(up_list)-1 > up_i  and timer >= (up_list[up_i]-4.9):
            new_up = Sprite("assets/UpArrow.png")
            new_up.set_position(-new_up.width, 11*screen.height/16)
            moving_arrows_up.append(new_up)
            up_i += 1
        if len(down_list)-1> down_i and timer >= (down_list[down_i]-4.9):
            new_down = Sprite("assets/down_arrow.png")
            new_down.set_position(-new_up.width, 12*screen.height/16)
            moving_arrows_down.append(new_down)
            down_i += 1
        if len(left_list)-1>left_i and timer >= (left_list[left_i]-4.9):
            new_left = Sprite("assets/left_arrow.png")
            new_left.set_position(-new_up.width, 13*screen.height/16)
            moving_arrows_left.append(new_left)
            left_i += 1
        if len(right_list)-1> right_i and timer >= (right_list[right_i]-4.9):
            new_right = Sprite("assets/right_arrow.png")
            new_right.set_position(-new_up.width, 14*screen.height/16)
            moving_arrows_right.append(new_right)
            right_i += 1

        #desenha setinhas e explosões na tela
        for arrow in moving_arrows_up:
            arrow.draw()
            arrow.move_x(arrows_speed*screen.delta_time())
        for arrow in moving_arrows_down:
            arrow.draw()
            arrow.move_x(arrows_speed*screen.delta_time())
        for arrow in moving_arrows_left:
            arrow.draw()
            arrow.move_x(arrows_speed*screen.delta_time())
        for arrow in moving_arrows_right:
            arrow.draw()
            arrow.move_x(arrows_speed*screen.delta_time())

        for xplosion in xplosion_list:
            xplosion.draw()
            xplosion.update()
            
        #remove as setas fora da tela das listas de setas para movimentar
        if len(moving_arrows_up)>0:
            if moving_arrows_up[0].x >= screen.width:
                resposta = "miss"
                moving_arrows_up.pop(0)
                score -= 30
                super_meter.height = 0
        if len(moving_arrows_down)>0:
            if moving_arrows_down[0].x >= screen.width:
                resposta = "miss"
                moving_arrows_down.pop(0)
                score -= 30
        if len(moving_arrows_left)>0:
            if moving_arrows_left[0].x>= screen.width:
                resposta = "miss"
                moving_arrows_left.pop(0)
                score -= 30
        if len(moving_arrows_right)>0:
            if moving_arrows_right[0].x >= screen.width:
                resposta = "miss"
                moving_arrows_right.pop(0)
                score -= 30
        
        if len(xplosion_list)>0 and xplosion_list[0].is_playing() == False:
            seta = xplosion_list.pop(0)
            seta.hide()
        
        #avalia o timing em que uma tecla foi apertada, contando a pontuação
        if keyboard.key_pressed("UP")and arrow_tick > 0.2:
            resposta = judge_inputs("UP", moving_arrows_up, super_meter, checker_right, xplosion_list)
            score += judge_resposta(resposta)
            arrow_tick = 0
        elif keyboard.key_pressed("DOWN") and arrow_tick > 0.2:
            resposta = judge_inputs('DOWN', moving_arrows_down, super_meter, checker_right, xplosion_list)
            score += judge_resposta(resposta)
            arrow_tick = 0
        elif keyboard.key_pressed("LEFT") and arrow_tick > 0.2:
            resposta = judge_inputs('LEFT', moving_arrows_left, super_meter, checker_right, xplosion_list)
            score += judge_resposta(resposta)
            arrow_tick = 0
        elif keyboard.key_pressed("right") and arrow_tick > 0.2:
            fx_right.draw()
            resposta = judge_inputs('right', moving_arrows_right, super_meter, checker_right, xplosion_list)
            score += judge_resposta(resposta)
            arrow_tick = 0
        else:
            arrow_tick += screen.delta_time()

        if keyboard.key_pressed("UP"):
            fx_up.draw()
        elif keyboard.key_pressed("left"):
            fx_left.draw()
        elif keyboard.key_pressed("right"):
            fx_right.draw()
        elif keyboard.key_pressed("down"):
            fx_down.draw()

        #ação do especial
        if keyboard.key_pressed("SPACE") and super_meter.height >=128:
            score += special_use(moving_arrows_up, xplosion_list)
            score += special_use(moving_arrows_down, xplosion_list)
            score += special_use(moving_arrows_right, xplosion_list)
            score += special_use(moving_arrows_left, xplosion_list)
            super_meter.height = 0

        if up_list[-1] < timer:
            music_is_on = False
            screen.draw_text(f'Finish!', screen.width/2, screen.height/8, color=(0,0,0), size=35)
            screen.draw_text(f'{score}', screen.width/2, screen.height/8+10, color=(0,0,0), size=35, font_name="segoeui")
