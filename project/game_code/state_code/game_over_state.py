from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import start_state
from project.game_code.state_code import title_state
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state

name = "GameOverState"
image = None


def enter():
    global image
    image = load_image('sprite\\state\\game-over.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.pop_state()


def draw():
    update_canvas()
    image.draw(480, 300, 960, 600)


def update():
    pass


def pause():
    pass


def resume():
    pass
