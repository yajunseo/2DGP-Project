from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import main_state

name = "PauseState"
image = None


def enter():
    global image
    image = load_image('sprite\\stat\\Game_pause.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    update_canvas()
    image.draw(480, 300, 300, 300)


def update():
    pass


def pause():
    pass


def resume():
    pass
