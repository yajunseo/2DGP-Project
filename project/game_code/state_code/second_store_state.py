from pico2d import *
from project.game_code.state_code import game_framework
from project.game_code.state_code import first_main_state
from project.game_code.state_code import second_main_state
from project.game_code.state_code import third_main_state


name = "StoreState"
image = None
door_close = None
door_open = None
speed_up = None
life_up = None
font = None
is_click = False
life = None
choose_button = 1
item_count = 0
speed_item_count = 0
buy_sound = None
door = None
no_money = None

def enter():
    global image, door_close, door_open, speed_up, life_up, font, life, buy_sound, door, no_money
    image = load_image('sprite\\state\\store.png')
    door_close = load_image('sprite\\state\\door_close.png')
    door_open = load_image('sprite\\state\\door_open.png')
    speed_up = load_image('sprite\\state\\attack_speed.png')
    life_up = load_image('sprite\\state\\1UP.png')
    font = load_font('font.TTF', 28)
    life = load_image('sprite\\Character\\life.png')
    buy_sound = load_wav('sound\\store.wav')
    buy_sound.set_volume(100)
    door = load_wav('sound\\door.wav')
    door.set_volume(80)
    no_money = load_wav('sound\\no_money.wav')
    no_money.set_volume(80)


def exit():
    global image
    del (image)


def handle_events():
    global choose_button, item_count, is_click, speed_item_count, buy_sound, door, no_money
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
                    if first_main_state.dragon.gold >= 500:
                        buy_sound.play()
                        item_count += 1
                        is_click = True
                        second_main_state.dragon.life += 1
                    else:
                        no_money.play()
                elif choose_button == 2:
                    if first_main_state.dragon.gold >= 500:
                        buy_sound.play()
                        item_count += 1
                        speed_item_count += 1
                        is_click = True
                    else:
                        no_money.play()
                else:
                    door.play()
                    game_framework.change_state(third_main_state)




def draw():
    global choose_button, font, life
    clear_canvas()
    image.draw(480, 300, 960, 600)
#    life.draw(40 + 20, 580, 40, 40)
    for i in range(second_main_state.dragon.life):
        life.draw(i * 40 + 20, 580, 40, 40)

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
    font.draw(830, 580, '%d' % first_main_state.dragon.gold, (255, 255, 255))

    update_canvas()


def update():
    global is_click, item_count
    if is_click:
        is_click = False
        first_main_state.dragon.gold -= (500*item_count)
        item_count = 0


def check_item_numer():
    return life_item_cnt, speed_item_cnt

def pause():
    pass


def resume():
    pass

def get_life():
    return second_main_state.dragon.life

def get_speed_item():
    return speed_item_count
