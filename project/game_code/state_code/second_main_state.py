import random
import json
import os
import time

from pico2d import *

from project.game_code.state_code import game_framework
from project.game_code.state_code import pause_state
from project.game_code.state_code import game_over_state
from project.game_code.state_code import store_state
from project.game_code.management_code import second_game_world

from project.game_code.object_code.dragon import Dragon
from project.game_code.object_code.tadpole import Tadpole
from project.game_code.object_code.drunk import Drunk
from project.game_code.object_code.bubble import Bubble
from project.game_code.stage_code.pink_background import Background

name = "second_main_state"

dragon = None
background = None
tadpoles = None
drunk = None
bubble = None
is_drunk_spawn = False
life = None


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
    global dragon, background, tadpoles, drunk, life
    dragon = Dragon()
    background = Background()
    tadpoles = [Tadpole(45, 157, 1),Tadpole(915, 157, -1), Tadpole(915, 373, -1),
               Tadpole(45, 373, 1), Tadpole(500, 157, -1),Tadpole(280, 373, 1),
               Tadpole(500, 265, 1),Tadpole(700, 373, -1)]
    drunk = Drunk()
    life = load_image('sprite\\Character\\life.png')

    second_game_world.add_object(background, 0)
    second_game_world.add_objects(tadpoles, 1)
    second_game_world.add_object(dragon, 2)


#    game_world.add_object(drunk, 3)


def exit():
    second_game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global bubble
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
            if event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
                dragon.check_attack_delay_end_time = get_time() - dragon.check_attack_delay_start_time
                if dragon.check_attack_delay_end_time > 0.3:
                    bubble = Bubble(dragon.x, dragon.y, dragon.dir)
                    second_game_world.add_object(bubble, 4)
                    dragon.check_attack_delay_end_time = 0
                    dragon.check_attack_delay_start_time = get_time()


def update():
    global is_drunk_spawn
    for game_object in second_game_world.all_objects():
        game_object.update()

    if dragon.is_fall:
        if bottom_collide(dragon, background, 12):
            dragon.stop()
        else:
            if not bottom_collide(dragon, background, 12):
                dragon.cancel_stop()

    for tadpole in tadpoles:
        if collide(dragon, tadpole):
            if not tadpole.is_beaten:
                if not dragon.is_beaten:
                    dragon.life -= 1
                    dragon.is_beaten = True
                    dragon.invincible_start_time = get_time()
            else:
                if not tadpole.is_dead:
                    tadpole.is_dead = True
                    tadpole.check_dead_motion_time = get_time()

    for tadpole in tadpoles:
        if tadpole.check_dead_motion_end_time > 1:
            second_game_world.remove_object(tadpole)

    if not second_game_world.objects[1]:
        if not is_drunk_spawn:
            second_game_world.add_object(drunk, 3)
            is_drunk_spawn = True

    if bubble:
        for tadpole in tadpoles:
            if collide(bubble, tadpole):
                if not tadpole.is_beaten:
                    second_game_world.remove_object(bubble)
                    tadpole.is_beaten = True

    # dragon -> bubble
    if second_game_world.objects[3]:
        if collide(bubble, drunk):
            second_game_world.remove_object(bubble)
            if drunk.hp > 0:
                drunk.hp -= 1
            else:
                if not drunk.is_lock:
                    drunk.is_lock = True

        if collide(dragon, drunk):
            if not drunk.is_lock:
                if not dragon.is_beaten:
                    dragon.life -= 1
                    dragon.is_beaten = True
                    dragon.invincible_start_time = get_time()
            else:
                if not drunk.is_dead:
                    drunk.check_dead_motion_start_time = get_time()
                    drunk.is_dead = True

        if drunk.check_dead_motion_end_time > 1:
            second_game_world.remove_object(drunk)
            game_framework.change_state(store_state)


def draw():
    clear_canvas()
    for game_object in second_game_world.all_objects():
        game_object.draw()
    for i in range(dragon.life):
        life.draw(i*40+20, 580, 40, 40)

    update_canvas()
