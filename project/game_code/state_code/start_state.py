from pico2d import *
import time
from project.game_code.state_code import game_framework
from project.game_code.state_code import title_state
from project.game_code.state_code import game_over_state

name = "StartState"
image = None
logo_time = 0.0
kpu_start_sound = None


def enter():
    global image, kpu_start_sound
    image = load_image('sprite\\state\\kpu_credit.png')
    kpu_start_sound = load_wav('sound\\kpu.wav')
    kpu_start_sound.set_volume(50)
    kpu_start_sound.play()


def exit():
    global image
    del image


def update():
    global logo_time
    logo_time = get_time()

    if logo_time > 3.5:
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
