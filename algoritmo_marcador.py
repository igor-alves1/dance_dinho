from PPlay.sprite import *
from PPlay.sound import *
from PPlay.gameimage import *
from PPlay.window import *

music = input("digite o nome do arquivo da musica: ")

up_file = open(f'{music}_up_file.txt', 'w')
down_file = open(f'{music}_down_file.txt', 'w')
right_file = open(f'{music}_right_file.txt', 'w')
left_file = open(f'{music}_left_file.txt', 'w')

screen = Window(600, 600)
teclado = screen.get_keyboard()

closer = Sound(f'{music}.ogg')
closer.set_volume(100)
played = False

music_meter = Sprite("music_meter.png")
music_meter.set_position(screen.width/2, screen.height/2)
music_meter.width = 0
time = 0

left_keys_times = []
right_keys_times = []
up_keys_times = []
down_keys_times = []
was_pressed = False
cooldown = 0.0

while True:
    screen.set_background_color((0,0,0))

    music_meter.draw()


    if time >= 1:
        music_meter.width += 1
        time = screen.delta_time()
    else:
        time += screen.delta_time()

    if teclado.key_pressed("UP") and was_pressed == False:
        up_keys_times.append(time+music_meter.width)
        print(f"UP, {time+music_meter.width}")
        up_file.write(str(time+music_meter.width)+" \n")
        was_pressed = True
    elif teclado.key_pressed("DOWN") and was_pressed == False:
        down_keys_times.append(time+music_meter.width)
        print(f"DOWN, {time+music_meter.width}")
        down_file.write(str(time+music_meter.width)+" \n")
        was_pressed = True
    elif teclado.key_pressed("RIGHT") and was_pressed == False:
        right_keys_times.append(time+music_meter.width)
        print(f"RIGHT, {time+music_meter.width}")
        right_file.write(str(time+music_meter.width)+" \n")
        was_pressed = True
    elif teclado.key_pressed("LEFT") and was_pressed == False:
        left_keys_times.append(time+music_meter.width)
        print(f"LEFT, {time+music_meter.width}")
        left_file.write(str(time+music_meter.width)+" \n")
        was_pressed = True
    else:
        if cooldown >= 0.200 and was_pressed == True:
            cooldown = 0
            was_pressed = False
        elif cooldown < 0.200 and was_pressed == True:
            cooldown += screen.delta_time()

    if teclado.key_pressed("P"):
        up_file.close()
        down_file.close()
        right_file.close()
        left_file.close()
        screen.close()
    
    if not played:
        closer.play()
        played = True
    screen.update()

