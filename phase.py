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
image_meter.set_position(15*screen.width/16, (screen.height-image_meter.height)/2)
super_meter = Sprite("meter.png")
super_meter.set_position(image_meter.x, image_meter.y)
super_meter.height = 0

every_one_s = 0

def judge_inputs(key_entered, arrows_array):
    if len(arrows_array)>0 and abs(arrows_array[0].x - checker_up.x) <= 10:
        return "perfect"
    else:
        return "miss"         
resposta = ""

while True:
    screen.set_background_color((0, 0, 0))
    checker_right.draw()
    checker_left.draw()
    checker_up.draw()
    checker_down.draw()
    image_meter.draw()
    super_meter.draw()
    
    if keyboard.key_pressed('enter') or start:
        countdown -= screen.delta_time()
        start = True
        screen.draw_text(f'{countdown:.0f}', screen.width/2, screen.height/8, color=(255,255,255))
        if countdown <= 0:
            start = False
            song.play()
            start_timer = True
    
    if start_timer:
        timer += screen.delta_time()
        screen.draw_text(f'{timer:.1f}  {resposta}', screen.width/2, screen.height/8, color=(255,255,255))
        if timer >= every_one_s+1:
            every_one_s += 1
            super_meter.height += 5

    if timer >= (up_list[up_i]-4.9):
        new_up = Sprite("UpArrow.png")
        new_up.set_position(-new_up.width, 11*screen.height/16)
        moving_arrows_up.append(new_up)
        up_i += 1
    if timer >= (down_list[down_i]-4.9):
        new_down = Sprite("down_arrow.png")
        new_down.set_position(-new_up.width, 12*screen.height/16)
        moving_arrows_down.append(new_down)
        down_i += 1
    if timer >= (left_list[left_i]-4.9):
        new_left = Sprite("left_arrow.png")
        new_left.set_position(-new_up.width, 13*screen.height/16)
        moving_arrows_left.append(new_left)
        left_i += 1
    if timer >= (right_list[right_i]-4.9):
        new_right = Sprite("right_arrow.png")
        new_right.set_position(-new_up.width, 14*screen.height/16)
        moving_arrows_right.append(new_right)
        right_i += 1

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

    if len(moving_arrows_up)> 0 and moving_arrows_up[0].x >= screen.width:
        x = moving_arrows_up.pop(0)
    if len(moving_arrows_down)> 0 and moving_arrows_down[0].x >= screen.width:
        x = moving_arrows_down.pop(0)
    if len(moving_arrows_left)> 0 and moving_arrows_left[0].x >= screen.width:
        x = moving_arrows_left.pop(0)
    if len(moving_arrows_right)> 0 and moving_arrows_right[0].x >= screen.width:
        x = moving_arrows_right.pop(0)

    if keyboard.key_pressed("UP"):
        resposta = judge_inputs('UP', moving_arrows_up)
    elif keyboard.key_pressed("DOWN"):
        resposta = judge_inputs('DOWN', moving_arrows_down)
    elif keyboard.key_pressed("LEFT"):
        resposta = judge_inputs('LEFT', moving_arrows_left)
    elif keyboard.key_pressed("right"):
        resposta = judge_inputs('right', moving_arrows_right)
        
    screen.update()
