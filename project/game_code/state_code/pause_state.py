from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state
from project.game_code.state_code import third_main_state
from project.game_code.state_code import title_state


name = "PauseState"
image = None
font_restart = None

def enter():
    global image, font_restart
    image = load_image('sprite\\state\\Game_pause.png')
    font_restart = load_font('font.TTF', 30)


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                game_framework.stack[-2].exit()
                game_framework.change_state(title_state)


def draw():
    update_canvas()
    image.draw(480, 300, 300, 300)
    font_restart.draw(330, 500, "resume : p", (255, 225, 0))
    font_restart.draw(330, 100, "restart : r", (255, 225, 0))

def update():
    pass


def pause():
    pass


def resume():
    pass
