from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import start_state
from project.game_code.state_code import title_state
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state
from project.game_code.state_code import third_main_state

name = "GameOverState"
image = None
game_over_sound = None

def enter():
    global image,game_over_sound
    image = load_image('sprite\\state\\game-over.png')

    game_over_sound = load_wav('sound\\gameover.wav')
    game_over_sound.set_volume(50)
    game_over_sound.play(1)


def exit():
    global image, game_over_sound
    del image
    del game_over_sound


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def draw():
    update_canvas()
    image.draw(480, 300, 960, 600)


def update():
    pass


def pause():
    pass


def resume():
    pass
