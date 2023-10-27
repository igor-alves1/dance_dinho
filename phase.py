from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sound import *

screen = Window(600, 600)
keyboard = screen.get_keyboard()

up_list, down_list, right_list, left_list = [], [], [], []

def readToList(doc_name, array):
    file = open(doc_name, 'r')

    for line in file:
        value = line.strip()
        time = float(value[:6])
        array.append(time)

    file.close()

music = input("digite o arquivo da musica: ")
song = Sound(f"docs/{music}/{music}.ogg")

readToList(f'docs/{music}/{music}_up_file.txt', up_list)
readToList(f'docs/{music}/{music}_down_file.txt', down_list)
readToList(f'docs/{music}/{music}_left_file.txt', left_list)
readToList(f'docs/{music}/{music}_right_file.txt', right_list)


arrows_speed = 140
arrow_tick = 0
up_i, down_i, left_i, right_i = 0, 0, 0, 0

timer = 0
start_timer = False
countdown = 3
start = False

moving_arrows_up, moving_arrows_down, moving_arrows_left, moving_arrows_right = [], [], [], []
music_is_on = True

checker_right = Sprite("right_check.png")
checker_right.set_position(14*screen.width/16, 14*screen.height/16)

checker_up = Sprite("up_checker.png")
checker_up.set_position(14*screen.width/16, 11*screen.height/16)

checker_down = Sprite("down_checker.png")
checker_down.set_position(14*screen.width/16, 12*screen.height/16)

checker_left = Sprite("left_checker.png")
checker_left.set_position(14*screen.width/16, 13*screen.height/16)

image_meter = GameImage("fix_meter.png")
image_meter.set_position(14*screen.width/16, 2*(screen.height-image_meter.height)/6)
super_meter = Sprite("meter.png")
super_meter.set_position(image_meter.x, image_meter.y)
super_meter.height = 0

def judge_inputs(key_entered, arrows_array, super_bar):
    if len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<5:
        arrows_array.pop(0)
        super_bar.height += 5
        return "perfect"
    elif len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<15:
        arrows_array.pop(0)
        return "good"
    elif len(arrows_array)>0 and abs(arrows_array[0].x-checker_right.x)<25:
        arrows_array.pop(0)
        return "ok"
    else:
        arrows_array.pop(0)
        super_bar.height = 0
        return "miss"

def judge_resposta(resposta):
    if resposta == "perfect":
        return 50
    elif resposta == "good":
        return 20
    elif resposta == "ok":
        return 10
    return -30
resposta = ""

score = 0

def special_use(moving_arrows_array):
    score_special = 50
    while len(moving_arrows_array)>0:
        moving_arrows_array.pop(0)
        score_special += 50

    return score_special

while True:
    screen.set_background_color((0, 0, 0))
    checker_right.draw()
    checker_left.draw()
    checker_up.draw()
    checker_down.draw()
    image_meter.draw()
    super_meter.draw()

    #inicia o countdown quando é apertada a tecla enter
    if keyboard.key_pressed('enter') or start:
        countdown -= screen.delta_time()
        start = True
        screen.draw_text(f'{countdown:.0f}', screen.width/2, screen.height/8, color=(255,255,255))
        if countdown <= 0:
            start = False
            song.play()
            start_timer = True
            
    #inicia o timer e exibe o timer e o score na tela
    if start_timer:
        timer += screen.delta_time()
        screen.draw_text(f'{timer:.1f}  {resposta}', screen.width/2, screen.height/8, color=(255,255,255))
        screen.draw_text(f'{score}', screen.width/2, screen.height/8+20, color=(255,255,255))

    #faz as setinhas surgirem com delay para chegarem do outro lado na tela no tempo certo
    if len(up_list)-1 > up_i  and timer >= (up_list[up_i]-4.9):
        new_up = Sprite("UpArrow.png")
        new_up.set_position(-new_up.width, 11*screen.height/16)
        moving_arrows_up.append(new_up)
        up_i += 1
    if len(down_list)-1> down_i and timer >= (down_list[down_i]-4.9):
        new_down = Sprite("down_arrow.png")
        new_down.set_position(-new_up.width, 12*screen.height/16)
        moving_arrows_down.append(new_down)
        down_i += 1
    if len(left_list)-1>left_i and timer >= (left_list[left_i]-4.9):
        new_left = Sprite("left_arrow.png")
        new_left.set_position(-new_up.width, 13*screen.height/16)
        moving_arrows_left.append(new_left)
        left_i += 1
    if len(right_list)-1> right_i and timer >= (right_list[right_i]-4.9):
        new_right = Sprite("right_arrow.png")
        new_right.set_position(-new_up.width, 14*screen.height/16)
        moving_arrows_right.append(new_right)
        right_i += 1

    #desenha setinhas na tela
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
        
    #remove as setas fora da tela das listas de setas para movimentar
    if len(moving_arrows_up)>0:
        if moving_arrows_up[0].x >= screen.width:
            resposta = "miss"
            moving_arrows_up.pop(0)
            score -= 30
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
    
    #avalia o timing em que uma tecla foi apertada, contando a pontuação
    if keyboard.key_pressed("UP") and arrow_tick > 0.3:
        resposta = judge_inputs("UP", moving_arrows_up, super_meter)
        score += judge_resposta(resposta)
        arrow_tick = 0
    elif keyboard.key_pressed("DOWN") and arrow_tick > 0.3:
        resposta = judge_inputs('DOWN', moving_arrows_down, super_meter)
        score += judge_resposta(resposta)
        arrow_tick = 0
    elif keyboard.key_pressed("LEFT") and arrow_tick > 0.3:
        resposta = judge_inputs('LEFT', moving_arrows_left, super_meter)
        score += judge_resposta(resposta)
        arrow_tick = 0
    elif keyboard.key_pressed("right") and arrow_tick > 0.3:
        resposta = judge_inputs('right', moving_arrows_right, super_meter)
        score += judge_resposta(resposta)
        arrow_tick = 0
    else:
        arrow_tick += screen.delta_time()

    #ação do especial
    if keyboard.key_pressed("SPACE") and super_meter.height >=128:
        score += special_use(moving_arrows_up)
        score += special_use(moving_arrows_down)
        score += special_use(moving_arrows_right)
        score += special_use(moving_arrows_left)
        super_meter.height = 0

    if up_list[-1] < timer:
        start_timer = False
        screen.draw_text(f'Finish!', screen.width/2, screen.height/8, color=(255,255,255))
        
    screen.update()
