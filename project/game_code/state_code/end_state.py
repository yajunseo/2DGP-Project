from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state

name = "EndState"
image = None
font = None
font_score = None
score = None
count = 0

def enter():
    global image, font, font_score, score, count
    image = load_image('sprite\\state\\end.png')
    font = load_font('font.TTF', 48)
    font_score = load_font('font.TTF', 30)
    count = 0
    score = second_main_state.get_gold()

def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()



def draw():
    global count
    clear_canvas()
    count += 1
    image.draw(480, 300, 960, 600)
    if count <= 60:
        font.draw(230, 130, 'GAME CLEAR', (255, 0, 0))
    else:
        font.draw(230, 130, 'GAME CLEAR', (255, 94, 0))
        if count >= 120:
            count = 0
    font_score.draw(330, 50, 'SCORE: %d'%score, (255, 255, 255))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
