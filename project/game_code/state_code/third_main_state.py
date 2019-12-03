import random
import json
import os
import time


from pico2d import *

from project.game_code.state_code import game_framework
from project.game_code.state_code import pause_state
from project.game_code.state_code import game_over_state
from project.game_code.state_code import second_store_state
from project.game_code.state_code import end_state
from project.game_code.state_code import first_main_state
from project.game_code.management_code import game_world

from project.game_code.object_code.dragon import Dragon
from project.game_code.object_code.pulpul import Pulpul
from project.game_code.object_code.drunk import Drunk
from project.game_code.object_code.bubble import Bubble
from project.game_code.object_code.bottle import Bottle
from project.game_code.object_code.item_banana import Banana
from project.game_code.object_code.item_turnip import Turnip
from project.game_code.object_code.item_watermelon import Watermelon
from project.game_code.stage_code.green_background import Background

name = "second_main_state"

dragon = None
background = None
pulpuls = None
drunk = None
bubble = None
bottle = None
is_drunk_spawn = False
life = None
font = None
speed_item_count = None
bananas = None
turnips = None
watermelons = None


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
    global dragon, background, pulpuls, drunk, life, font, gold, bottle, speed_item_count, is_drunk_spawn
    is_drunk_spawn = False
    speed_item_count = second_store_state.get_speed_item()
    dragon = Dragon()
    dragon.life = second_store_state.get_life()
    background = Background()
    pulpuls = [Pulpul(500, 25, 1), Pulpul(800, 25, -1), Pulpul(220, 130, -1),
              Pulpul(760, 130, 1), Pulpul(315, 240, -1), Pulpul(435, 349, 1),
              Pulpul(220, 445, 1), Pulpul(750, 455, -1)]
    drunk = Drunk()
    life = load_image('sprite\\Character\\life.png')

    game_world.add_object(background, 0)
    game_world.add_objects(pulpuls, 1)
    game_world.add_object(dragon, 2)
    font = load_font('font.TTF', 28)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global bubble, speed_item_count
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
                if dragon.check_attack_delay_end_time > (0.3 - speed_item_count*0.1):
                    bubble = Bubble(dragon.x, dragon.y, dragon.dir)
                    game_world.add_object(bubble, 4)
                    dragon.check_attack_delay_end_time = 0
                    dragon.check_attack_delay_start_time = get_time()


def update():
    global is_drunk_spawn, bottle, bananas, turnips, watermelons
    for game_object in game_world.all_objects():
        game_object.update()

    if dragon.y <= 26:
        dragon.y = 540
    if dragon.is_fall:
        if bottom_collide(dragon, background, 14):
            dragon.stop()
        else:
            if not bottom_collide(dragon, background, 14):
                dragon.cancel_stop()

    for pulpul in pulpuls:
        if pulpul.y <= 26:
            pulpul.y = 540

        if bottom_collide(pulpul, background, 14):
            pulpul.is_fall = False
        else:
            pulpul.is_fall = True
        if collide(dragon, pulpul):
            if not pulpul.is_beaten:
                if not dragon.is_beaten:
                    if dragon.life >= 0:
                        dragon.life -= 1

                    dragon.is_beaten = True
                    dragon.invincible_start_time = get_time()
            else:
                if not pulpul.is_dead:
                    first_main_state.dragon.gold += 100
                    pulpul.is_dead = True
                    fruit_random_spawn_percent = random.randint(1, 200)
                    if fruit_random_spawn_percent <= 60:
                        bananas = Banana(pulpul.x, pulpul.y)
                        game_world.add_object(bananas, 6)
                        bananas.spawn_start_time = get_time()
                    elif fruit_random_spawn_percent <= 110:
                        turnips = Turnip(pulpul.x, pulpul.y)
                        game_world.add_object(turnips, 6)
                        turnips.spawn_start_time = get_time()
                    elif fruit_random_spawn_percent <= 140:
                        watermelons = Watermelon(pulpul.x, pulpul.y)
                        game_world.add_object(watermelons, 6)
                        watermelons.spawn_start_time = get_time()
                    pulpul.check_dead_motion_time = get_time()
                    pulpul.check_dead_motion_time = get_time()

    for pulpul in pulpuls:
        if pulpul.check_dead_motion_end_time > 1:
            game_world.remove_object(pulpul)

    if game_world.objects[6]:
        for i in game_world.objects[6]:
            if i.spawn_check_time > 1:
                i.is_spawn = True
        for i in game_world.objects[6]:
            if i.is_spawn:
                if collide(dragon, i):
                    if i.number == 1:
                        dragon.gold += 50
                    elif i.number == 2:
                        dragon.gold += 100
                    else:
                        dragon.gold += 200
                    game_world.remove_object(i)

    if not game_world.objects[1]:
        if not is_drunk_spawn:
            game_world.add_object(drunk, 3)
            is_drunk_spawn = True

    if game_world.objects[4]:
        for pulpul in pulpuls:
            for i in game_world.objects[4]:
                if collide(i, pulpul):
                    if not pulpul.is_beaten:
                        game_world.remove_object(i)
                        pulpul.is_beaten = True

    # dragon -> bubble
    if game_world.objects[3]:
        if game_world.objects[4]:
            for i in game_world.objects[4]:
                if collide(i, drunk):
                    game_world.remove_object(i)
                    if drunk.hp >= 0:
                        drunk.hp -= 1
                    else:
                        if not drunk.is_lock:
                            drunk.is_lock = True

        if not drunk.is_lock:
            if drunk.check_attack_end_time > (0.5 - (drunk.phase * 0.1)):
                bottle = Bottle(drunk.x, drunk.y, drunk.phase, drunk.bottle_number)
                game_world.add_object(bottle, 5)
                drunk.bottle_number = (drunk.bottle_number + 1) % 16
                drunk.check_attack_start_time = get_time()

        if collide(dragon, drunk):
            if not drunk.is_lock:
                if not dragon.is_beaten:
                    if dragon.life >= 0:
                        dragon.life -= 1
                    dragon.is_beaten = True
                    dragon.invincible_start_time = get_time()
            else:
                if not drunk.is_dead:
                    first_main_state.dragon.gold += 500
                    drunk.check_dead_motion_start_time = get_time()
                    drunk.is_dead = True

        if drunk.check_dead_motion_end_time > 1:
            game_world.remove_object(drunk)
            game_framework.change_state(end_state)

    if not drunk.is_dead:
        if bottle:
            for i in game_world.objects[5]:
                if collide(dragon, i):
                    if not dragon.is_beaten:
                        if dragon.life > 0:
                            dragon.life -= 1
                        dragon.is_beaten = True
                        dragon.invincible_start_time = get_time()
                        game_world.remove_object(i)
                else:
                    if i.x < 0 or i.x > 960 or i.y < 0 or i.y > 550:
                        game_world.remove_object(i)

    if dragon.life < 0:
        game_framework.change_state(game_over_state)

def draw():
    global font, gold
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    for i in range(dragon.life):
        life.draw(i*40+20, 580, 40, 40)
    font.draw(830, 580, '%d' % first_main_state.dragon.gold, (255, 255, 255))
    update_canvas()

def get_gold():
    return first_main_state.dragon.gold
