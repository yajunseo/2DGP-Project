from pico2d import *
import time
from project.game_code.state_code import game_framework
from project.game_code.state_code import title_state
from project.game_code.state_code import game_over_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('sprite\\state\\kpu_credit.png')




def exit():
    global image
    del image


def update():
    global logo_time
    logo_time = get_time()

    if logo_time > 2.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)


def draw():
    global image
    clear_canvas()
    image.draw(480, 300, 960, 600)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass
