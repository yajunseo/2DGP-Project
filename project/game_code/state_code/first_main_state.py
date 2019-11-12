import random
import json
import os

from pico2d import *

from project.game_code.state_code import game_framework
from project.game_code.state_code import pause_state
from project.game_code.object_code import game_world

from project.game_code.object_code.dragon import Dragon
from project.game_code.object_code.walker import Walker
from project.game_code.object_code.drunk import Drunk
from project.game_code.stage_code.blue_background import Background

name = "first_main_state"

dragon = None
background = None
walkers = None
drunk = None


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def bottom_collide(a, b, n):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    i = b.get_bb()
    for j in range(n):
        if left_a <= i[j][2] and right_a >= i[j][0]:
            if i[j][3] + 1 >= bottom_a >= i[j][3] - 1:
                return True
    return False


def enter():
    global dragon, background, walkers, drunk
    dragon = Dragon()
    background = Background()
    walkers = [Walker(230, 155, 1), Walker(740, 155, -1), Walker(500, 410, -1),
               Walker(510, 410, 1), Walker(320, 240, -1), Walker(650, 240, 1),
               Walker(230, 325, 1), Walker(740, 325, -1)]
    drunk = Drunk()

    game_world.add_object(background, 0)
    game_world.add_object(dragon, 1)
    game_world.add_objects(walkers, 2)
    game_world.add_object(drunk, 3)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            dragon.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if dragon.is_fall:
        if bottom_collide(dragon, background, 8):
            dragon.stop()
        else:
            if not bottom_collide(dragon, background, 8):
                dragon.cancel_stop()


    for walker in walkers:
        if collide(dragon, walker):
            if not dragon.is_hit:
                dragon.life -= 1
                dragon.is_hit = True
                dragon.invincible_start_time = get_time()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
