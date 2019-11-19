from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state


name = "StoreState"
image = None
door_close = None
door_open = None
speed_up = None
life_up = None
choose_button = 1
life_item_cnt = 0
speed_item_cnt = 0


def enter():
    global image, door_close, door_open, speed_up, life_up
    image = load_image('sprite\\state\\store.png')
    door_close = load_image('sprite\\state\\door_close.png')
    door_open = load_image('sprite\\state\\door_open.png')
    speed_up = load_image('sprite\\state\\shoe-512.png')
    life_up = load_image('sprite\\state\\1UP.png')


def exit():
    global image
    del (image)


def handle_events():
    global choose_button, life_item_cnt, speed_item_cnt
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if choose_button > 1:
                    choose_button -= 1

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if choose_button < 3:
                    choose_button += 1

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if choose_button == 1:
                    life_item_cnt += 1
                elif choose_button == 2:
                    speed_item_cnt += 1
                else:
                    game_framework.change_state(second_main_state)




def draw():
    global choose_button
    clear_canvas()
    image.draw(480, 300, 960, 600)
    if choose_button == 1:
        life_up.draw(230, 430, 150, 150)
        speed_up.draw(480, 430, 70, 70)
        door_close.draw(730, 430, 70, 70)

    elif choose_button == 2:
        life_up.draw(230, 430, 70, 70)
        speed_up.draw(480, 430, 150, 150)
        door_close.draw(730, 430, 70, 70)

    else:
        life_up.draw(230, 430, 70, 70)
        speed_up.draw(480, 430, 70, 70)
        door_open.draw(730, 430, 150, 150)
    update_canvas()


def update():
    pass

def check_item_numer():
    return life_item_cnt, speed_item_cnt

def pause():
    pass


def resume():
    pass
