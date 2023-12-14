from PPlay.window import *
from menu import *
from select import *
from phase import *
from shop import *
from select import *

GAME_STATE = 1
GAME_SCREEN = Window(600, 600)

while True:
    if GAME_STATE == 1:
        GAME_STATE = menu(GAME_SCREEN)
    elif GAME_STATE == 2:
        GAME_STATE = phase(GAME_SCREEN)
    elif GAME_STATE == 3:
        GAME_STATE = shop(GAME_SCREEN)
    elif GAME_STATE == 4:
        GAME_STATE = select(GAME_SCREEN)
