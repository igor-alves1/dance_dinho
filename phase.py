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
song = Sound(f"{music}.ogg")

readToList(f'{music}_up_file.txt', up_list)
readToList(f'{music}_down_file.txt', down_list)
readToList(f'{music}_left_file.txt', left_list)
readToList(f'{music}_right_file.txt', right_list)

arrows_speed = 80
up_i = 0

timer = 0
start_timer = False
countdown = 3
start = False

moving_arrows = []
music_is_on = True

while True:
    screen.set_background_color((0, 0, 0))
    
    if keyboard.key_pressed('enter') or start:
        countdown -= screen.delta_time()
        start = True
        screen.draw_text(f'{countdown:.0f}', screen.width/2, screen.height/4, color=(255,255,255))
        if countdown <= 0:
            start = False
            start_timer = True
    
    if start_timer:
        song.play()
        timer += screen.delta_time()
        screen.draw_text(f'{timer:.1f}', screen.width/2, screen.height/4, color=(255,255,255))

    if music_is_on and timer >= (up_list[up_i]-7.5):
        new_up = Sprite("UpArrow.png")
        new_up.set_position(0, 3*screen.height/4)
        moving_arrows.append(new_up)
        up_i += 1
        
        if up_i > len(up_list)-1:
            music_is_on = False

    for arrow in moving_arrows:
        arrow.draw()
        arrow.move_x(arrows_speed * screen.delta_time())

    if moving_arrows[0].x >= screen.width:
        moving_arrows.pop[0]
        
    screen.update()
